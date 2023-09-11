from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///restaurant_database.db')

Base = declarative_base()
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())

    reviews = relationship("Review", back_populates="restaurant")
    # customers = relationship("Customer", secondary="reviews", back_populates="restaurants")
    customers = relationship("Customer", secondary="reviews", back_populates="restaurants", overlaps="reviews")

    # get all reviews for this restaurant
    @property
    def restaurant_reviews(self):
        return self.reviews
    
    # get the customers who reviewed this restaurant
    @property
    def restaurant_customers(self):
        return [review.customer for review in self.reviews]
    
    #fanciest restaurant
    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()
    
    #all reviews for this restaurant
    def all_reviews(self):
        formatted_reviews = []
        for review in self.reviews:
            formatted_review = f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
            formatted_reviews.append(formatted_review)
        return formatted_reviews

    def __repr__(self):
        return f'Restaurant {self.name}  Price: ${self.price}.00\n'
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())

    # reviews = relationship("Review", back_populates="customer")
    # restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers")
    reviews = relationship("Review", back_populates="customer", overlaps="customers")
    restaurants = relationship("Restaurant", secondary="reviews", back_populates="customers", overlaps="reviews")

    #customer reviews
    @property
    def customer_reviews(self):
        return self.reviews
    
    #customer restaurants
    @property
    def customer_restaurants(self):
        return self.restaurants

    #full name of the customer
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    #favorite restaurant of the customer
    def favorite_restaurant(self):
        highest_rating = 0
        favorite = None
        for review in self.reviews:
            if review.star_rating > highest_rating:
                highest_rating = review.star_rating
                favorite = review.restaurant
        return favorite
    
    #add a review for a restaurant
    def add_review(self, session, restaurant, rating):
        get_review = Review(
            restaurant_id=restaurant.id,
            customer=self,
            description="",
            star_rating=rating
        )
        session.add(get_review)
        session.commit()
        return get_review
    
   # delete all reviews for a restaurant
    def delete_reviews(self, session: Session, restaurant):
        session.query(Review).filter(
            Review.customer == self,
            Review.restaurant == restaurant
        ).delete(synchronize_session=False)

        session.commit()

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}'
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    description = Column(String())
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    star_rating = Column(Integer())

    # restaurant = relationship("Restaurant", back_populates="reviews")
    # customer = relationship("Customer", back_populates="reviews")
    restaurant = relationship("Restaurant", back_populates="reviews", overlaps="customers,restaurants")
    customer = relationship("Customer", back_populates="reviews", overlaps="customers,restaurants")
    
    #full review
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

    
    #instances
    @property
    def review_restaurant(self):
        return self.restaurant

    

    def __repr__(self):
        return f'{self.id}, {self.description}, {self.star_rating}'
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

# class Restaurant(Base):
#     __tablename__ = 'restaurants'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)

#     # Define the many-to-many relationship with Customer
#     customers = relationship('Customer', secondary='reviews')
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Define a one-to-many relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

    @classmethod
    def fanciest(cls):
        fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
        if not fanciest_restaurant:
            return "No restaurants available"
        return fanciest_restaurant

# class Customer(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)

#     # Define the many-to-many relationship with Restaurant
#     restaurants = relationship('Restaurant', secondary='reviews')
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # Define the one-to-many relationship with Review
    reviews = relationship('Review', back_populates='customer')
# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer, primary_key=True)
#     star_rating = Column(Integer, nullable=False)
#     customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
#     restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

#     customer = relationship('Customer', back_populates='reviews')
#     restaurant = relationship('Restaurant', back_populates='reviews')
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), nullable=False)

    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews') 
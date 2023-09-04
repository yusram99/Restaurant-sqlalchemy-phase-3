from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

# Review methods
def customer(review_id):
    review = session.query(Review).get(review_id)
    return review.customer

def restaurant(review_id):
    review = session.query(Review).get(review_id)
    return review.restaurant

# Restaurant methods
def reviews(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    return restaurant.reviews

def customers(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    return [review.customer for review in restaurant.reviews]

# Customer methods
def reviews(customer_id):
    customer = session.query(Customer).get(customer_id)
    return customer.reviews

def restaurants(customer_id):
    customer = session.query(Customer).get(customer_id)
    return [review.restaurant for review in customer.reviews]

# Additional methods
def full_name(customer_id):
    customer = session.query(Customer).get(customer_id)
    return f'{customer.first_name} {customer.last_name}'

def favorite_restaurant(customer_id):
    customer = session.query(Customer).get(customer_id)
    reviews = customer.reviews
    max_rating = max(reviews, key=lambda review: review.star_rating)
    return max_rating.restaurant

def add_review(customer_id, restaurant_id, star_rating):
    customer = session.query(Customer).get(customer_id)
    restaurant = session.query(Restaurant).get(restaurant_id)
    new_review = Review(star_rating=star_rating, customer=customer, restaurant=restaurant)
    session.add(new_review)
    session.commit()

def delete_reviews(customer_id, restaurant_id):
    customer = session.query(Customer).get(customer_id)
    restaurant = session.query(Restaurant).get(restaurant_id)
    reviews_to_delete = session.query(Review).filter_by(customer=customer, restaurant=restaurant).all()
    for review in reviews_to_delete:
        session.delete(review)
    session.commit()

def full_review(review_id):
    review = session.query(Review).get(review_id)
    return f'Review for {review.restaurant.name} by {full_name(review.customer.id)}: {review.star_rating} stars'

def fanciest():
    return session.query(Restaurant).order_by(Restaurant.price.desc()).first()

def all_reviews(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    return [full_review(review.id) for review in restaurant.reviews]

# # Example usage
# if __name__ == '__main__':
#     # Test your methods here


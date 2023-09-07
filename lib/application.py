# application.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Review, Customer, Restaurant, Base
from models import session


# Initialize the database
engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)
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

# Additional methods for Customer
def full_name(customer_id):
    customer = session.query(Customer).get(customer_id)
    return f'{customer.first_name} {customer.last_name}'

def favorite_restaurant(customer_id):
    customer = session.query(Customer).get(customer_id)
    reviews = customer.reviews
    if not reviews:
        return "No reviews available"
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

# Review full_review method
def full_review(review_id):
    review = session.query(Review).get(review_id)
    if not review:
        return "Review not found"
    return f'Review for {review.restaurant.name} by {full_name(review.customer.id)}: {review.star_rating} stars'

# Restaurant class method
@classmethod
def fanciest(cls):
    fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
    if not fanciest_restaurant:
        return "No restaurants available"
    return fanciest_restaurant

# Restaurant all_reviews method
def all_reviews(restaurant_id):
    restaurant = session.query(Restaurant).get(restaurant_id)
    if not restaurant:
        return "Restaurant not found"
    return [full_review(review.id) for review in restaurant.reviews]

# # Example usage
# if __name__ == '__main__':
#     # Create a new review for a customer
#     add_review(1, 1, 4)  # Add a review with star rating 4 for Restaurant A by Customer John Doe

#     # Retrieve and print customer's reviews
#     johns_reviews = reviews(1)  # Get reviews for Customer John Doe
#     for review in johns_reviews:
#         print(f"Review for {review.restaurant.name}: {review.star_rating} stars")

#     # Retrieve and print restaurants reviewed by a customer
#     johns_restaurants = restaurants(1)  # Get restaurants reviewed by Customer John Doe
#     for restaurant in johns_restaurants:
#         print(f"{restaurant.name} was reviewed by John Doe")

#     # Retrieve and print a restaurant's reviews
#     restaurant_a_reviews = all_reviews(1)  # Get all reviews for Restaurant A
#     for review in restaurant_a_reviews:
#         print(review)

#     # Find the fanciest restaurant
#     fanciest_restaurant = Restaurant.fanciest()  # Correct
#     print(f"The fanciest restaurant is {fanciest_restaurant.name}")

#     # Find John Doe's favorite restaurant
#     johns_favorite = favorite_restaurant(1)  # Get John Doe's favorite restaurant
#     print(f"{johns_favorite.name} is John Doe's favorite restaurant")

#     # Delete all of John Doe's reviews for Restaurant A
#     delete_reviews(1, 1)  # Delete John Doe's reviews for Restaurant A

#     # Confirm the reviews have been deleted
#     restaurant_a_reviews = all_reviews(1)  # Get all reviews for Restaurant A again
#     if not restaurant_a_reviews:
#         print("John Doe's reviews for Restaurant A have been deleted")
#     else:
#         print("Deletion failed")

#     # Test the full_review method for a specific review
#     review_text = full_review(1)  # Get the full review text for a review with ID 1
#     print(review_text)


if __name__ == '__main__':
    # Create a new review for a customer
    add_review(1, 1, 4)  # Add a review with star rating 4 for Restaurant A by Customer John Doe

    # Retrieve and print customer's reviews
    johns_reviews = reviews(1)  # Get reviews for Customer John Doe
    for review in johns_reviews:
        print(f"Review for {review.restaurant.name}: {review.star_rating} stars")

    # Retrieve and print restaurants reviewed by a customer
    johns_restaurants = restaurants(1)  # Get restaurants reviewed by Customer John Doe
    for restaurant in johns_restaurants:
        print(f"{restaurant.name} was reviewed by John Doe")

    # Retrieve and print a restaurant's reviews
    restaurant_a_reviews = all_reviews(1)  # Get all reviews for Restaurant A
    for review in restaurant_a_reviews:
        print(review)

    # Find the fanciest restaurant
    fanciest_restaurant = Restaurant.fanciest()
    print(f"The fanciest restaurant is {fanciest_restaurant.name}")

    # Find John Doe's favorite restaurant
    johns_favorite = favorite_restaurant(1)  # Get John Doe's favorite restaurant
    print(f"{johns_favorite.name} is John Doe's favorite restaurant")

    # Delete all of John Doe's reviews for Restaurant A
    delete_reviews(1, 1)  # Delete John Doe's reviews for Restaurant A

    # Confirm the reviews have been deleted
    restaurant_a_reviews = all_reviews(1)  # Get all reviews for Restaurant A again
    if not restaurant_a_reviews:
        print("John Doe's reviews for Restaurant A have been deleted")
    else:
        print("Deletion failed")

    # Test the full_review method for a specific review
    review_text = full_review(1)  # Get the full review text for a review with ID 1
    print(review_text)
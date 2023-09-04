from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=4)
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')
review1 = Review(star_rating=5, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=4, customer=customer2, restaurant=restaurant1)
review3 = Review(star_rating=3, customer=customer1, restaurant=restaurant2)

# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()
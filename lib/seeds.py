#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review
from models import Base, engine

Base.metadata.create_all(engine)

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restaurant_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# clear old data
session.query(Restaurant).delete()
session.query(Customer).delete()
session.query(Review).delete()
session.commit()


# Add a console message so we can see output when the seed file runs
print("Seeding Restaurant info...")

restaurants = [
    Restaurant(
        name=fake.name(),
        price=random.randint(1000, 50000)
    )
for i in range(10)]

session.add_all(restaurants)
session.commit()

print("Seeding Customers info...")

customers = [
    Customer(
        first_name=fake.first_name(),
        last_name = fake.last_name()
    )
for i in range(10)]

session.add_all(customers)
session.commit()

print("Seeding Reviews info...")

for restaurant in restaurants:
        for i in range(random.randint(1, 10)):
            customer = random.choice(customers)
            review = Review(
                restaurant_id=restaurant.id,
                description=fake.sentence(),
                star_rating=random.randint(1, 10),
                customer_id=customer.id
            )
            session.add(review)
    
session.commit()
session.close()
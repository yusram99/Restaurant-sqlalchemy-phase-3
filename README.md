# Restaurant Review Project

This project is a simple restaurant review system built using SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) library. It allows users to review restaurants and track their favorite dining experiences.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project consists of the following components:

- **Models**: SQLAlchemy models for `Restaurant`, `Customer`, and `Review` to represent restaurants, customers, and their reviews. These models define the database schema and relationships.

- **Migrations**: Alembic migration scripts to create and update the database schema.

- **Application**: An example application (`application.py`) that demonstrates how to interact with the database using SQLAlchemy queries and methods.

- **Seeds**: A seed script (`seeds.py`) to populate the database with sample data for testing.

## Installation

- Clone the repository to your local machine:
git clone https://github.com/your-username/restaurant-review-project.git

- Create a virtual environment (optional but recommended):
$python -m venv venv
$source venv/bin/activate

- Install project dependencies:
$pip install -r requirements.txt

- Create the database and apply migrations:
$alembic upgrade head

# Usage
- Run the application to test the database interactions:
$python application.py


# Directory Structure
The project directory structure is organized as follows:

restaurant_review_project/
│
├── application.py        # Example application code
├── models.py             # SQLAlchemy model definitions
├── migrations/           # Alembic migration scripts (auto-generated)
│
├── seeds.py              # Seed script to populate the database
├── README.md             # This README file
├── requirements.txt      # Project dependencies
│
└── restaurant_reviews.db  # SQLite database file (will be created)

# Contributing
Contributions to this project are welcome. If you find any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.


# Ecommerce Product Category Page

This is a Django project for managing and displaying products.

## Getting Started
Follow these instructions to set up and run the project on your local machine.

### Prerequisites
- Django==4.2.1
- Pillow==9.5.0

### Installation

- git clone: https://github.com/br25/       Ecommerce_product_category_page.git


- virtualenv create: 1. virtualenv venv
                     2. source venv/bin/activate

- pip install -r requirements.txt

- python manage.py makemigrations

- python manage.py migrate

- python manage.py createsuperuser

- python manage.py loaddata products.json

- python manage.py runserver
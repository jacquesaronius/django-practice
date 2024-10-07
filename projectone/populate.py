import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectone.settings')

import django
django.setup()

from faker import Faker
from appone.models import User


faker = Faker()

def create_user(first_name: str, last_name: str, email: str) -> User:

    user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
    user.save()
    
    return user


def populate_users(N: int = 5):
    for i in range(N):
        first_name = faker.first_name
        last_name = faker.last_name
        email = faker.email
        create_user(first_name, last_name, email)


if __name__ == "__main__":

    print("Populating database with models")    
    print("Populating Users")
    populate_users(10)
    print("User population complete")
    print("Population complete")        

    
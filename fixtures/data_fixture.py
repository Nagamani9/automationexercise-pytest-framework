import pytest
from faker import Faker


fake = Faker()

@pytest.fixture()
def generated_user():

    return {
        "name": fake.first_name(),
        "email": fake.email(),
        "password": "Password123"
    }
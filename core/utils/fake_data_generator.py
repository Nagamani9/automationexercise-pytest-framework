import time

from faker import Faker


fake = Faker()


class FakeDataGenerator:

    @staticmethod
    def generate_email():

        timestamp = int(time.time())

        return f"automation_{timestamp}@test.com"

    @staticmethod
    def generate_first_name():

        return fake.first_name()

    @staticmethod
    def generate_last_name():

        return fake.last_name()

    @staticmethod
    def generate_company():

        return fake.company()

    @staticmethod
    def generate_address():

        return fake.street_address()

    @staticmethod
    def generate_city():

        return fake.city()

    @staticmethod
    def generate_state():

        return fake.state()

    @staticmethod
    def generate_zipcode():

        return fake.postcode()

    @staticmethod
    def generate_mobile_number():

        return fake.msisdn()[:10]
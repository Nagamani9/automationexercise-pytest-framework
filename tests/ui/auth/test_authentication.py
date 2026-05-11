# tests/ui/auth/test_authentication.py

import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from core.utils.data_loader import DataLoader
from core.utils.assertions import Assertions
from core.utils.fake_data_generator import FakeDataGenerator


@allure.feature("Authentication")
class TestRegistration:

    @allure.story("Register New User")
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_register_new_user(
            self,
            driver
    ):

        data = DataLoader.load_json(
            "test_data/auth/register_user.json"
        )

        # =====================================
        # Dynamic Test Data
        # =====================================

        email = (
            FakeDataGenerator.generate_email()
        )

        first_name = (
            FakeDataGenerator.generate_first_name()
        )

        last_name = (
            FakeDataGenerator.generate_last_name()
        )

        company = (
            FakeDataGenerator.generate_company()
        )

        address = (
            FakeDataGenerator.generate_address()
        )

        city = (
            FakeDataGenerator.generate_city()
        )

        state = (
            FakeDataGenerator.generate_state()
        )

        zipcode = (
            FakeDataGenerator.generate_zipcode()
        )

        mobile_number = (
            FakeDataGenerator.generate_mobile_number()
        )

        # =====================================
        # Page Objects
        # =====================================

        home_page = HomePage(driver)

        signup_page = SignupPage(driver)

        # =====================================
        # Open Home Page
        # =====================================

        home_page.open()

        assert home_page.is_home_page_visible(), \
            "Home page is not visible"

        # =====================================
        # Navigate To Signup
        # =====================================

        home_page.click_signup_login()

        # =====================================
        # Signup
        # =====================================

        signup_page.enter_signup_name(
            data["name"]
        )

        signup_page.enter_signup_email(
            email
        )

        signup_page.click_signup()

        # =====================================
        # Verify Account Information
        # =====================================

        assert signup_page.is_account_information_visible(), \
            "Enter Account Information is not visible"

        # =====================================
        # Fill Account Information
        # =====================================

        signup_page.fill_account_information(

            password=data["password"],

            day=data["day"],
            month=data["month"],
            year=data["year"],

            first_name=first_name,
            last_name=last_name,

            company=company,

            address1=address,
            address2=address,

            country=data["country"],

            state=state,
            city=city,

            zipcode=zipcode,

            mobile_number=mobile_number
        )

        # =====================================
        # Create Account
        # =====================================

        signup_page.click_create_account()

        assert signup_page.is_account_created_visible(), \
            "Account Created message is not visible"

        # =====================================
        # Continue
        # =====================================

        signup_page.click_continue()

        assert home_page.is_logged_in_as_visible(), \
            "Logged in username is not visible"

        # =====================================
        # Delete Account
        # =====================================

        home_page.click_delete_account()

        assert signup_page.is_account_deleted_visible(), \
            "Account Deleted message is not visible"

        signup_page.click_continue()


    @allure.story("Register Existing Email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.ui
    def test_register_existing_email(
            self,
            driver
    ):

        data = DataLoader.load_json(
            "test_data/auth/login_data.json"
        )

        existing_user = data["valid_user"]

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open()
        assert home_page.is_home_page_visible(), "Home page is not visible"

        login_page.navigate_to_login()

        login_page.enter_signup_name("Test User")

        login_page.enter_signup_email(
            existing_user["email"]
        )

        login_page.click_signup()

        actual_error = login_page.get_signup_error_message()

        Assertions.assert_equals(
            actual_error,
            "Email Address already exist!"
        )


@allure.feature("Authentication - Login")
class TestLogin:

    @allure.story("Valid Login using correct credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login_with_valid_credentials(
            self,
            driver
    ):

        data = DataLoader.load_json(
            "test_data/auth/login_data.json"
        )

        user = data["valid_user"]

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open()
        assert home_page.is_home_page_visible(), "Home page is not visible"

        login_page.navigate_to_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        logged_in_text = (
            login_page.get_logged_in_username()
        )

        Assertions.assert_contains(
            logged_in_text,
            "Logged in as"
        )


    @allure.story("Invalid Login Using Wrong Credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "email,password",
        [
            ("wrong@test.com", "Password123"),  # wrong email
            ("abc@test.com", "wrong"),  # wrong password
        ]
    )
    def test_login_with_invalid_credentials(
            self,
            driver,
            email,
            password
    ):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open()
        login_page.navigate_to_login()
        login_page.login(
            email,
            password
        )

        actual_error = (
            login_page.get_login_error_message()
        )

        Assertions.assert_equals(
            actual_error,
            "Your email or password is incorrect!"
        )


    @allure.story("Invalid Login Using Empty Credentials")
    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "email,password,field",
        [
            ("", "Password123", "email"),
            ("abc@test.com", "", "password"),
            ("", "", "both")
        ]
    )
    def test_login_with_empty_credentials(self,driver,email,password,field):

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open()
        login_page.navigate_to_login()
        login_page.login(
            email,
            password
        )

        if field=="email":
            validation_message=login_page.get_email_validation_message()
            assert validation_message!=""
            assert "fill" in validation_message.lower()

        elif field=="password":
            validation_message=login_page.get_password_validation_message()
            assert validation_message!=""
            assert "fill" in validation_message.lower()

        elif field=="both":
            validation_message=login_page.get_email_validation_message()
            assert validation_message!=""
            assert "fill" in validation_message.lower()






@allure.feature("Authentication - Logout")
class TestSession:

    @allure.story("Logout")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.ui
    def test_logout_user(
            self,
            driver
    ):

        data = DataLoader.load_json(
            "test_data/auth/login_data.json"
        )

        user = data["valid_user"]

        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.open()

        login_page.navigate_to_login()

        login_page.login(
            user["email"],
            user["password"]
        )

        login_page.logout()

        current_url = driver.current_url

        Assertions.assert_contains(
            current_url,
            "login"
        )
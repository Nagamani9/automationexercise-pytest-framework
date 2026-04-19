import pytest
from pages.signup_page import SignupPage

def test_register_user(driver):
    signup=SignupPage(driver)

    # Verify home page
    print(driver.current_url)
    assert "automationexercise" in driver.current_url

    # next step
    signup.go_to_signup()

    # next step
    assert signup.is_new_user_visible()
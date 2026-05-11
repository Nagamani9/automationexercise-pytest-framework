from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[text()=' Signup / Login']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT  = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    SIGNUP_NAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH,"//button[@data-qa='signup-button']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(),'incorrect')]")
    SIGNUP_ERROR_MESSAGE = ( By.XPATH, "//p[contains(text(),'already exist!')]")
    LOGOUT_BUTTON = ( By.XPATH, "//a[contains(text(),'Logout')]")
    LOGGED_IN_USER = ( By.XPATH, "//a[contains(text(),'Logged in as')]")

    def navigate_to_login(self):
        self.safe_click(self.LOGIN_LINK)

    def login(self, email, password):
        self.enter_text(self.LOGIN_EMAIL_INPUT, email)
        self.enter_text(self.LOGIN_PASSWORD_INPUT, password)
        self.safe_click(self.LOGIN_BUTTON)

    def enter_signup_name(self, name):
        self.enter_text(self.SIGNUP_NAME_INPUT,name)

    def enter_signup_email(self, email):
            self.enter_text(self.SIGNUP_EMAIL_INPUT,email)

    def click_signup(self):
        self.safe_click(self.SIGNUP_BUTTON)

    def get_login_error_message(self):
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    def get_signup_error_message(self):
        return self.get_text(self.SIGNUP_ERROR_MESSAGE)

    def logout(self):
        self.safe_click(self.LOGOUT_BUTTON)

    def get_logged_in_username(self):
        return self.get_text(self.LOGGED_IN_USER)

    def get_email_validation_message(self):
        return self.get_validation_message(
            self.LOGIN_EMAIL_INPUT
        )

    def get_password_validation_message(self):
        return self.get_validation_message(
            self.LOGIN_PASSWORD_INPUT
        )
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):

    # Navigation
    signup_login_btn=(By.XPATH, "//a[contains(text(),' Signup / Login')]")

    # New User Sign Up! step 1
    new_user_text=(By.XPATH,"//h2[text()='New User Signup!']")

    # Actions
    def go_to_signup(self):
        self.click(self.signup_login_btn)

    def is_new_user_visible(self):
        return self.is_element_visible(self.new_user_text)




from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    HOME_PAGE_LOGO = (By.XPATH,"//img[@alt='Website for automation practice']")
    SIGNUP_LOGIN_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Signup / Login')]"
    )

    LOGGED_IN_AS_TEXT = (
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )

    DELETE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Delete Account')]"
    )

    def is_home_page_visible(self):
        return self.is_element_visible(self.HOME_PAGE_LOGO)

    def open(self,path=""):
        super().open()

    def click_signup_login(self):
        self.safe_click(
            self.SIGNUP_LOGIN_BUTTON
        )

    def is_logged_in_as_visible(self):
        return self.is_element_visible(
            self.LOGGED_IN_AS_TEXT
        )

    def click_delete_account(self):
        self.safe_click(
            self.DELETE_ACCOUNT_BUTTON
        )
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from core.utils.waits import WaitUtils
from core.config.config_manager import ConfigManager
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException
)



class BasePage:

    def __init__(self, driver):
        self.driver=driver

    def open(self, path=""):
        base_url = ConfigManager.get(
            "base_url"
        )

        self.driver.get(
            f"{base_url}{path}"
        )

    def safe_click(self,locator, retries=3):

        for retry in range(retries):
            try:
                element=self.wait_for_clickable(locator)
                element.click()
                return

            except (ElementClickInterceptedException, StaleElementReferenceException):
                if retry==retries-1:
                    self.js_click(locator)

    def wait_for_clickable(self,locator):
        return WaitUtils.clickable(self.driver, locator)

    def enter_text(self, locator, text):

        element = WaitUtils.visible(self.driver, locator)

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):

        element = WaitUtils.visible(self.driver, locator)
        return element.text

    def is_element_visible(self, locator):

        try:

            return WaitUtils.visible(self.driver,locator)

        except TimeoutException:

            return False

    def select_dropdown_by_visible_text( self,locator,text):

        element = self.driver.find_element(*locator)
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def get_validation_message(self, locator):

        element = self.driver.find_element(*locator)
        return self.driver.execute_script("return arguments[0].validationMessage;",element)

    def js_click(self, locator):

        element = WaitUtils.visible(self.driver,locator)
        self.driver.execute_script("arguments[0].click();",element)

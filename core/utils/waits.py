from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.config.config_manager import ConfigManager


class WaitUtils:

    @staticmethod
    def visible(driver, locator):
        timeout=ConfigManager.get("timeouts")["explicit_wait"]
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def clickable(driver, locator):
        timeout = ConfigManager.get("timeouts")["explicit_wait"]
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @staticmethod
    def invisible(driver, locator):
        timeout = ConfigManager.get("timeouts")["explicit_wait"]
        return WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

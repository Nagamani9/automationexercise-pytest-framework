from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from core.config.config_manager import ConfigManager


class DriverFactory:

    @staticmethod
    def get_driver():

        browser = ConfigManager.get("browser")

        if browser.lower() == "chrome":

            options = webdriver.ChromeOptions()
            options.page_load_strategy = 'eager'

            if ConfigManager.get("headless"):
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        else:
            raise Exception(f"Unsupported browser: {browser}")

        driver.maximize_window()

        driver.implicitly_wait(
            ConfigManager.get("timeouts")["implicit_wait"]
        )

        driver.set_page_load_timeout(
            ConfigManager.get("timeouts")["page_load"]
        )

        return driver
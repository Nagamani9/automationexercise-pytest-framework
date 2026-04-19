import pytest
import os

from utils.config_reader import load_config
from utils.driver_factory import get_driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            driver.save_screenshot(f"screenshots/{item.name}.png")

@pytest.fixture
def driver():
    config = load_config()
    browser = config["browser"]  # ✅ get from config
    driver = get_driver(browser)
    driver.get(config["base_url"])
    yield driver
    driver.quit()
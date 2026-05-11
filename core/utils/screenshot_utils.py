import os
from datetime import datetime


class ScreenshotUtils:

    @staticmethod
    def save_screenshot(driver, name):

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        path = f"screenshots/{name}_{timestamp}.png"

        driver.save_screenshot(path)

        return path
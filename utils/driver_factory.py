from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# def get_driver(browser):
#     if browser == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # raise ValueError(f"Unsupported browser: {browser}"
def get_driver(browser):
    options = webdriver.ChromeOptions()

    # ✅ REQUIRED for GitHub Actions
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
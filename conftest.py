import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import BROWSER, HEADLESS, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT, BASE_URL


def get_driver():
    if BROWSER == "firefox":
        opts = FirefoxOptions()
        if HEADLESS:
            opts.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
    else:
        opts = ChromeOptions()
        if HEADLESS:
            opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-extensions")
        opts.add_argument("--proxy-server=direct://")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver


@pytest.fixture(scope="function")
def driver():
    d = get_driver()
    d.get(BASE_URL)
    yield d
    d.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    from pages.login_page import LoginPage
    from config import TEST_EMAIL, TEST_PASSWORD
    login = LoginPage(driver)
    login.open()
    login.login(TEST_EMAIL, TEST_PASSWORD)
    yield driver

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL


class SignupPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstname'], input[name='first_name'], #firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastname'], input[name='last_name'], #lastname")
    EMAIL = (By.CSS_SELECTOR, "input[type='email'], input[name='email'], #email")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password'], input[id='password']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='confirm_password'], input[name='password_confirmation']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, ".error, .alert-danger, [class*='error']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success, .success, [class*='success']")

    def open(self):
        self.driver.get(f"{BASE_URL}/register")
        return self

    def register(self, first_name, last_name, email, password, confirm_password=None):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        if confirm_password:
            self.type(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.SUBMIT)

    def is_error_shown(self):
        return self.is_visible(self.ERROR_MSG)

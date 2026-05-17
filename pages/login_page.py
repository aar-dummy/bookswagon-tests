from selenium.webdriver.common.by import By
from bookswagon_tests.pages.base_page import BasePage
from bookswagon_tests.config import BASE_URL


class LoginPage(BasePage):
    EMAIL = (By.CSS_SELECTOR, "input[type='email'], input[name='email'], #email")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password'], input[name='password'], #password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit'], .login-btn")
    ERROR_MSG = (By.CSS_SELECTOR, ".error, .alert-danger, .error-message, [class*='error']")
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Forgot') or contains(@href,'forgot')]")

    def open(self):
        self.driver.get(f"{BASE_URL}/login")
        return self

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def is_error_shown(self):
        return self.is_visible(self.ERROR_MSG)

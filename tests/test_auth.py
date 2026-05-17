import pytest
from bookswagon_tests.pages.login_page import LoginPage
from bookswagon_tests.pages.signup_page import SignupPage
from bookswagon_tests.config import TEST_EMAIL, TEST_PASSWORD, BASE_URL
import time


class TestLogin:
    def test_login_page_loads(self, driver):
        page = LoginPage(driver)
        page.open()
        assert page.is_visible(page.EMAIL)
        assert page.is_visible(page.PASSWORD)
        assert page.is_visible(page.SUBMIT)

    def test_login_with_invalid_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("invalid@example.com", "wrongpassword")
        assert page.is_error_shown() or "login" in driver.current_url.lower()

    def test_login_with_empty_fields(self, driver):
        page = LoginPage(driver)
        page.open()
        page.click(page.SUBMIT)
        # Should stay on login page or show validation
        assert "login" in driver.current_url.lower() or page.is_error_shown()

    def test_login_with_valid_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login(TEST_EMAIL, TEST_PASSWORD)
        # After login, should redirect away from login page
        time.sleep(2)
        assert "login" not in driver.current_url.lower() or "account" in driver.current_url.lower()

    def test_forgot_password_link_visible(self, driver):
        page = LoginPage(driver)
        page.open()
        assert page.is_visible(page.FORGOT_PASSWORD)


class TestSignup:
    def test_signup_page_loads(self, driver):
        page = SignupPage(driver)
        page.open()
        assert page.is_visible(page.EMAIL)
        assert page.is_visible(page.PASSWORD)

    def test_signup_with_existing_email(self, driver):
        page = SignupPage(driver)
        page.open()
        page.register("Test", "User", TEST_EMAIL, TEST_PASSWORD, TEST_PASSWORD)
        assert page.is_error_shown() or "register" in driver.current_url.lower()

    def test_signup_with_empty_fields(self, driver):
        page = SignupPage(driver)
        page.open()
        page.click(page.SUBMIT)
        assert "register" in driver.current_url.lower() or page.is_error_shown()

    def test_signup_with_invalid_email(self, driver):
        page = SignupPage(driver)
        page.open()
        page.register("Test", "User", "notanemail", TEST_PASSWORD, TEST_PASSWORD)
        assert page.is_error_shown() or "register" in driver.current_url.lower()

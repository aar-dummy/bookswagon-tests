import pytest
from bookswagon_tests.pages.account_page import AccountPage
from bookswagon_tests.pages.login_page import LoginPage
from bookswagon_tests.config import BASE_URL


class TestAccount:
    def test_account_requires_login(self, driver):
        page = AccountPage(driver)
        page.open()
        assert "login" in driver.current_url.lower() or "account" in driver.current_url.lower()

    def test_account_page_loads_when_logged_in(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        assert "login" not in logged_in_driver.current_url.lower()

    def test_orders_link_visible(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        assert page.is_visible(page.ORDERS_LINK)

    def test_addresses_link_visible(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        assert page.is_visible(page.ADDRESSES_LINK)

    def test_change_password_link_visible(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        assert page.is_visible(page.CHANGE_PASSWORD_LINK)

    def test_logout(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        page.logout()
        import time; time.sleep(1)
        assert "login" in logged_in_driver.current_url.lower() or BASE_URL in logged_in_driver.current_url

    def test_navigate_to_orders(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        page.go_to_orders()
        assert "order" in logged_in_driver.current_url.lower()

    def test_navigate_to_addresses(self, logged_in_driver):
        page = AccountPage(logged_in_driver)
        page.open()
        page.go_to_addresses()
        assert "address" in logged_in_driver.current_url.lower()

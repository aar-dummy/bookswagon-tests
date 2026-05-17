import pytest
from bookswagon_tests.pages.home_page import HomePage
from bookswagon_tests.config import BASE_URL


class TestHomePage:
    def test_homepage_loads(self, driver):
        page = HomePage(driver)
        page.open()
        assert BASE_URL in driver.current_url

    def test_logo_visible(self, driver):
        page = HomePage(driver)
        page.open()
        assert page.is_logo_visible()

    def test_search_box_visible(self, driver):
        page = HomePage(driver)
        page.open()
        assert page.is_search_visible()

    def test_page_title_contains_bookswagon(self, driver):
        page = HomePage(driver)
        page.open()
        assert "bookswagon" in driver.title.lower()

    def test_nav_links_present(self, driver):
        page = HomePage(driver)
        page.open()
        for locator in [page.NAV_BOOKS, page.NAV_FICTION, page.NAV_KIDS, page.NAV_EXAMS]:
            assert page.is_visible(locator), f"Nav link not visible: {locator}"

    def test_cart_icon_visible(self, driver):
        page = HomePage(driver)
        page.open()
        assert page.is_visible(page.CART_ICON)

    def test_login_link_visible(self, driver):
        page = HomePage(driver)
        page.open()
        assert page.is_visible(page.LOGIN_LINK)

    def test_search_redirects(self, driver):
        from bookswagon_tests.config import SEARCH_QUERY
        page = HomePage(driver)
        page.open()
        page.search(SEARCH_QUERY)
        assert "search" in driver.current_url.lower() or SEARCH_QUERY.split()[0].lower() in driver.current_url.lower()

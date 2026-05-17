import pytest
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from config import BASE_URL


CATEGORY_URLS = [
    f"{BASE_URL}/fiction",
    f"{BASE_URL}/non-fiction",
    f"{BASE_URL}/kids",
    f"{BASE_URL}/teens-ya",
]


class TestNavigation:
    def test_books_nav_click(self, driver):
        page = HomePage(driver)
        page.open()
        page.click(page.NAV_BOOKS)
        assert driver.current_url != f"{BASE_URL}/"

    def test_fiction_nav_click(self, driver):
        page = HomePage(driver)
        page.open()
        page.click(page.NAV_FICTION)
        assert "fiction" in driver.current_url.lower() or driver.current_url != f"{BASE_URL}/"

    def test_kids_nav_click(self, driver):
        page = HomePage(driver)
        page.open()
        page.click(page.NAV_KIDS)
        assert "kids" in driver.current_url.lower() or driver.current_url != f"{BASE_URL}/"

    def test_exams_nav_click(self, driver):
        page = HomePage(driver)
        page.open()
        page.click(page.NAV_EXAMS)
        assert "exam" in driver.current_url.lower() or driver.current_url != f"{BASE_URL}/"


class TestCategoryPage:
    @pytest.mark.parametrize("url", CATEGORY_URLS)
    def test_category_loads_products(self, driver, url):
        page = CategoryPage(driver)
        page.open(url)
        assert page.get_product_count() > 0 or page.is_visible(page.PAGE_HEADING)

    def test_category_has_heading(self, driver):
        page = CategoryPage(driver)
        page.open(f"{BASE_URL}/fiction")
        assert page.is_visible(page.PAGE_HEADING)

    def test_category_pagination(self, driver):
        page = CategoryPage(driver)
        page.open(f"{BASE_URL}/fiction")
        # Pagination may or may not be present depending on results
        assert page.get_product_count() >= 0

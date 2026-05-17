import pytest
from bookswagon_tests.pages.search_results_page import SearchResultsPage
from bookswagon_tests.pages.product_detail_page import ProductDetailPage
from bookswagon_tests.config import SEARCH_QUERY


def navigate_to_product(driver):
    """Helper: search and click first result to land on a product page."""
    search = SearchResultsPage(driver)
    search.open(SEARCH_QUERY)
    search.click_first_result()
    return ProductDetailPage(driver)


class TestProductDetailPage:
    def test_product_title_visible(self, driver):
        page = navigate_to_product(driver)
        assert page.is_visible(page.TITLE)

    def test_product_price_visible(self, driver):
        page = navigate_to_product(driver)
        assert page.is_visible(page.PRICE)

    def test_add_to_cart_button_visible(self, driver):
        page = navigate_to_product(driver)
        assert page.is_add_to_cart_visible()

    def test_product_has_title_text(self, driver):
        page = navigate_to_product(driver)
        title = page.get_title()
        assert len(title) > 0

    def test_product_has_price_text(self, driver):
        page = navigate_to_product(driver)
        price = page.get_price()
        assert len(price) > 0

    def test_add_to_cart_guest(self, driver):
        """Adding to cart as guest should either succeed or prompt login."""
        page = navigate_to_product(driver)
        page.add_to_cart()
        # Either cart count increases or login prompt appears
        assert "cart" in driver.current_url.lower() or page.is_visible(page.CART_SUCCESS) or "login" in driver.current_url.lower()

    def test_breadcrumb_visible(self, driver):
        page = navigate_to_product(driver)
        assert page.is_visible(page.BREADCRUMB)

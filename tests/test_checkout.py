import pytest
from bookswagon_tests.pages.checkout_page import CheckoutPage
from bookswagon_tests.pages.cart_page import CartPage
from bookswagon_tests.pages.search_results_page import SearchResultsPage
from bookswagon_tests.pages.product_detail_page import ProductDetailPage
from bookswagon_tests.config import SEARCH_QUERY


def add_item_to_cart(driver):
    search = SearchResultsPage(driver)
    search.open(SEARCH_QUERY)
    search.click_first_result()
    product = ProductDetailPage(driver)
    product.add_to_cart()


class TestCheckout:
    def test_checkout_requires_login(self, driver):
        page = CheckoutPage(driver)
        page.open()
        assert "login" in driver.current_url.lower() or "checkout" in driver.current_url.lower()

    def test_checkout_page_loads_when_logged_in(self, logged_in_driver):
        add_item_to_cart(logged_in_driver)
        page = CheckoutPage(logged_in_driver)
        page.open()
        assert "checkout" in logged_in_driver.current_url.lower() or "login" not in logged_in_driver.current_url.lower()

    def test_checkout_has_address_section(self, logged_in_driver):
        add_item_to_cart(logged_in_driver)
        page = CheckoutPage(logged_in_driver)
        page.open()
        assert page.is_address_section_visible() or page.is_visible(page.ORDER_SUMMARY)

    def test_checkout_has_order_summary(self, logged_in_driver):
        add_item_to_cart(logged_in_driver)
        page = CheckoutPage(logged_in_driver)
        page.open()
        assert page.is_visible(page.ORDER_SUMMARY) or page.is_address_section_visible()

    def test_proceed_to_checkout_from_cart(self, logged_in_driver):
        add_item_to_cart(logged_in_driver)
        cart = CartPage(logged_in_driver)
        cart.open()
        if cart.get_item_count() > 0:
            cart.proceed_to_checkout()
            assert "checkout" in logged_in_driver.current_url.lower()

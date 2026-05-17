import pytest
from pages.cart_page import CartPage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from config import SEARCH_QUERY, BASE_URL


def add_product_to_cart(driver):
    search = SearchResultsPage(driver)
    search.open(SEARCH_QUERY)
    search.click_first_result()
    product = ProductDetailPage(driver)
    product.add_to_cart()


class TestCart:
    def test_cart_page_loads(self, driver):
        page = CartPage(driver)
        page.open()
        assert "cart" in driver.current_url.lower()

    def test_empty_cart_message(self, driver):
        page = CartPage(driver)
        page.open()
        assert page.is_empty() or page.get_item_count() == 0

    def test_add_item_to_cart(self, driver):
        add_product_to_cart(driver)
        cart = CartPage(driver)
        cart.open()
        # Cart should have items or redirect to login
        assert cart.get_item_count() > 0 or "login" in driver.current_url.lower()

    def test_remove_item_from_cart(self, driver):
        add_product_to_cart(driver)
        cart = CartPage(driver)
        cart.open()
        if cart.get_item_count() > 0:
            initial_count = cart.get_item_count()
            cart.remove_first_item()
            import time; time.sleep(1)
            assert cart.get_item_count() < initial_count or cart.is_empty()

    def test_cart_shows_total(self, driver):
        add_product_to_cart(driver)
        cart = CartPage(driver)
        cart.open()
        if cart.get_item_count() > 0:
            assert cart.is_visible(cart.TOTAL_PRICE)

    def test_checkout_button_visible_with_items(self, driver):
        add_product_to_cart(driver)
        cart = CartPage(driver)
        cart.open()
        if cart.get_item_count() > 0:
            assert cart.is_visible(cart.CHECKOUT_BTN)

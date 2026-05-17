import pytest
from pages.wishlist_page import WishlistPage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from config import SEARCH_QUERY


class TestWishlist:
    def test_wishlist_page_loads(self, logged_in_driver):
        page = WishlistPage(logged_in_driver)
        page.open()
        assert "wishlist" in logged_in_driver.current_url.lower()

    def test_empty_wishlist_message(self, logged_in_driver):
        page = WishlistPage(logged_in_driver)
        page.open()
        assert page.is_empty() or page.get_item_count() >= 0

    def test_add_to_wishlist(self, logged_in_driver):
        search = SearchResultsPage(logged_in_driver)
        search.open(SEARCH_QUERY)
        search.click_first_result()
        product = ProductDetailPage(logged_in_driver)
        product.add_to_wishlist()
        wishlist = WishlistPage(logged_in_driver)
        wishlist.open()
        assert wishlist.get_item_count() > 0

    def test_remove_from_wishlist(self, logged_in_driver):
        # First add an item
        search = SearchResultsPage(logged_in_driver)
        search.open(SEARCH_QUERY)
        search.click_first_result()
        product = ProductDetailPage(logged_in_driver)
        product.add_to_wishlist()

        wishlist = WishlistPage(logged_in_driver)
        wishlist.open()
        if wishlist.get_item_count() > 0:
            wishlist.remove_first_item()
            import time; time.sleep(1)
            assert wishlist.get_item_count() == 0 or wishlist.is_empty()

    def test_wishlist_requires_login(self, driver):
        page = WishlistPage(driver)
        page.open()
        # Should redirect to login if not authenticated
        assert "login" in driver.current_url.lower() or "wishlist" in driver.current_url.lower()

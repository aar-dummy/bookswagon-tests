from selenium.webdriver.common.by import By
from bookswagon_tests.pages.base_page import BasePage
from bookswagon_tests.config import BASE_URL


class WishlistPage(BasePage):
    WISHLIST_ITEMS = (By.CSS_SELECTOR, ".wishlist-item, [class*='wishlist-item']")
    EMPTY_MSG = (By.CSS_SELECTOR, ".empty-wishlist, [class*='empty']")
    REMOVE_BTN = (By.CSS_SELECTOR, ".remove-wishlist, [class*='remove']")
    MOVE_TO_CART = (By.XPATH, "//button[contains(text(),'Add to Cart') or contains(text(),'Move to Cart')]")

    def open(self):
        self.driver.get(f"{BASE_URL}/wishlist")
        return self

    def get_item_count(self):
        return len(self.driver.find_elements(*self.WISHLIST_ITEMS))

    def is_empty(self):
        return self.is_visible(self.EMPTY_MSG)

    def remove_first_item(self):
        items = self.driver.find_elements(*self.REMOVE_BTN)
        if items:
            items[0].click()

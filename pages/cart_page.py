from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item, .cart-product, [class*='cart-item']")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".empty-cart, [class*='empty-cart']")
    REMOVE_BTN = (By.CSS_SELECTOR, ".remove-item, .delete-item, [class*='remove']")
    CHECKOUT_BTN = (By.XPATH, "//button[contains(text(),'Checkout') or contains(text(),'Proceed')]//ancestor-or-self::a | //a[contains(text(),'Checkout')]")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".cart-total, .total-price, [class*='total']")
    QTY_INPUT = (By.CSS_SELECTOR, "input[name='quantity'], .qty-input")
    UPDATE_BTN = (By.XPATH, "//button[contains(text(),'Update')]")

    def open(self):
        self.driver.get(f"{BASE_URL}/cart")
        return self

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def is_empty(self):
        return self.is_visible(self.EMPTY_CART_MSG)

    def remove_first_item(self):
        items = self.driver.find_elements(*self.REMOVE_BTN)
        if items:
            items[0].click()

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

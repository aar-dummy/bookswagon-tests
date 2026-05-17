from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "h1.product-title, h1, .book-title h1")
    PRICE = (By.CSS_SELECTOR, ".price, .product-price, [class*='price']")
    ADD_TO_CART = (By.XPATH, "//button[contains(text(),'Add to Cart') or contains(text(),'Add To Cart')]")
    ADD_TO_WISHLIST = (By.XPATH, "//button[contains(text(),'Wishlist') or contains(@class,'wishlist')]")
    AUTHOR = (By.CSS_SELECTOR, ".author, [class*='author']")
    DESCRIPTION = (By.CSS_SELECTOR, ".description, .product-description, [class*='description']")
    QUANTITY = (By.CSS_SELECTOR, "input[name='quantity'], .qty-input, #quantity")
    CART_SUCCESS = (By.CSS_SELECTOR, ".cart-success, .alert-success, [class*='success']")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb, nav[aria-label='breadcrumb']")

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_price(self):
        return self.get_text(self.PRICE)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)

    def is_add_to_cart_visible(self):
        return self.is_visible(self.ADD_TO_CART)

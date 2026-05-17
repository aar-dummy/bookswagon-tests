from selenium.webdriver.common.by import By
from bookswagon_tests.pages.base_page import BasePage
from bookswagon_tests.config import BASE_URL


class CheckoutPage(BasePage):
    ADDRESS_SECTION = (By.CSS_SELECTOR, ".address-section, [class*='address']")
    PAYMENT_SECTION = (By.CSS_SELECTOR, ".payment-section, [class*='payment']")
    ORDER_SUMMARY = (By.CSS_SELECTOR, ".order-summary, [class*='order-summary']")
    PLACE_ORDER_BTN = (By.XPATH, "//button[contains(text(),'Place Order') or contains(text(),'Pay')]")
    COUPON_INPUT = (By.CSS_SELECTOR, "input[name*='coupon'], input[placeholder*='coupon'], #coupon")
    APPLY_COUPON = (By.XPATH, "//button[contains(text(),'Apply')]")
    LOGIN_REQUIRED_MSG = (By.CSS_SELECTOR, ".login-required, [class*='login']")

    def open(self):
        self.driver.get(f"{BASE_URL}/checkout")
        return self

    def is_address_section_visible(self):
        return self.is_visible(self.ADDRESS_SECTION)

    def is_payment_section_visible(self):
        return self.is_visible(self.PAYMENT_SECTION)

    def apply_coupon(self, code):
        self.type(self.COUPON_INPUT, code)
        self.click(self.APPLY_COUPON)

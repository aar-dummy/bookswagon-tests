from selenium.webdriver.common.by import By
from bookswagon_tests.pages.base_page import BasePage
from bookswagon_tests.config import BASE_URL


class AccountPage(BasePage):
    ORDERS_LINK = (By.XPATH, "//a[contains(text(),'Orders') or contains(@href,'orders')]")
    ADDRESSES_LINK = (By.XPATH, "//a[contains(text(),'Addresses') or contains(@href,'addresses')]")
    SETTINGS_LINK = (By.XPATH, "//a[contains(text(),'Settings') or contains(@href,'settings')]")
    CHANGE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Password') or contains(@href,'password')]")
    GIFT_CERT_LINK = (By.XPATH, "//a[contains(text(),'Gift') or contains(@href,'gift')]")
    LOGOUT_LINK = (By.XPATH, "//a[contains(text(),'Log out') or contains(text(),'Logout')]")
    ACCOUNT_HEADING = (By.CSS_SELECTOR, "h1, .account-title, .page-title")

    def open(self):
        self.driver.get(f"{BASE_URL}/account")
        return self

    def go_to_orders(self):
        self.click(self.ORDERS_LINK)

    def go_to_addresses(self):
        self.click(self.ADDRESSES_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)

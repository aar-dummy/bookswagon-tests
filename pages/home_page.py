from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config import BASE_URL


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand img, .logo img, img[alt*='Bookswagon']")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search'], input[placeholder*='Search'], #search-input, input[name='search']")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit'], .search-btn, .search-icon")
    NAV_BOOKS = (By.XPATH, "//nav//a[contains(text(),'Books')]")
    NAV_FICTION = (By.XPATH, "//nav//a[contains(text(),'Fiction')]")
    NAV_NON_FICTION = (By.XPATH, "//nav//a[contains(text(),'Non-Fiction') or contains(text(),'Non Fiction')]")
    NAV_TEENS = (By.XPATH, "//nav//a[contains(text(),'Teens') or contains(text(),'YA')]")
    NAV_KIDS = (By.XPATH, "//nav//a[contains(text(),'Kids')]")
    NAV_EXAMS = (By.XPATH, "//nav//a[contains(text(),'Exams')]")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='cart'], .cart-icon, .cart-link")
    WISHLIST_ICON = (By.CSS_SELECTOR, "a[href*='wishlist'], .wishlist-icon")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Log in') or contains(text(),'Login') or contains(@href,'login')]")
    SIGNUP_LINK = (By.XPATH, "//a[contains(text(),'Sign up') or contains(text(),'Register') or contains(@href,'register')]")
    BANNER = (By.CSS_SELECTOR, ".banner, .carousel, .slider, .hero-banner")

    def open(self):
        self.driver.get(BASE_URL)
        return self

    def search(self, query):
        self.type(self.SEARCH_BOX, query)
        self.find(self.SEARCH_BOX).send_keys(Keys.RETURN)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def go_to_wishlist(self):
        self.click(self.WISHLIST_ICON)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def go_to_signup(self):
        self.click(self.SIGNUP_LINK)

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

    def is_search_visible(self):
        return self.is_visible(self.SEARCH_BOX)

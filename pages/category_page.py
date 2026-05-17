from selenium.webdriver.common.by import By
from bookswagon_tests.pages.base_page import BasePage


class CategoryPage(BasePage):
    PRODUCTS = (By.CSS_SELECTOR, ".product-item, .book-item, .product-card")
    FILTER_SECTION = (By.CSS_SELECTOR, ".filters, .filter-section, [class*='filter']")
    SORT_SELECT = (By.CSS_SELECTOR, "select[name*='sort'], .sort-select")
    PAGINATION = (By.CSS_SELECTOR, ".pagination, [class*='pagination']")
    PAGE_HEADING = (By.CSS_SELECTOR, "h1, .page-title, .category-title")
    PRICE_FILTER = (By.CSS_SELECTOR, "[class*='price-filter'], .price-range")

    def open(self, url):
        self.driver.get(url)
        return self

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCTS))

    def get_heading(self):
        return self.get_text(self.PAGE_HEADING)

    def is_filter_visible(self):
        return self.is_visible(self.FILTER_SECTION)

    def is_pagination_visible(self):
        return self.is_visible(self.PAGINATION)

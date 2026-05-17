from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL


class SearchResultsPage(BasePage):
    RESULTS = (By.CSS_SELECTOR, ".product-item, .book-item, .product-card, [class*='product']")
    RESULT_TITLES = (By.CSS_SELECTOR, ".product-title, .book-title, h3 a, .title a")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, ".no-results, .empty-results, [class*='no-result']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select[name*='sort'], .sort-select, #sort-by")
    FILTER_PRICE = (By.CSS_SELECTOR, ".price-filter, [class*='price-filter']")
    PAGINATION_NEXT = (By.CSS_SELECTOR, "a[rel='next'], .pagination .next, li.next a")
    RESULT_COUNT = (By.CSS_SELECTOR, ".result-count, .showing-results, [class*='result-count']")

    def open(self, query):
        self.driver.get(f"{BASE_URL}/search-books/{query.replace(' ', '+')}")
        return self

    def get_results(self):
        try:
            return self.driver.find_elements(*self.RESULTS)
        except Exception:
            return []

    def results_count(self):
        return len(self.get_results())

    def is_no_results_shown(self):
        return self.is_visible(self.NO_RESULTS_MSG)

    def click_first_result(self):
        results = self.get_results()
        if results:
            results[0].click()

    def go_to_next_page(self):
        self.click(self.PAGINATION_NEXT)

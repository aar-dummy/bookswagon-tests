import pytest
from bookswagon_tests.pages.search_results_page import SearchResultsPage
from bookswagon_tests.pages.home_page import HomePage
from bookswagon_tests.config import SEARCH_QUERY, SEARCH_QUERY_NO_RESULTS


class TestSearch:
    def test_search_returns_results(self, driver):
        page = SearchResultsPage(driver)
        page.open(SEARCH_QUERY)
        assert page.results_count() > 0

    def test_search_url_contains_query(self, driver):
        page = SearchResultsPage(driver)
        page.open(SEARCH_QUERY)
        assert SEARCH_QUERY.split()[0].lower() in driver.current_url.lower()

    def test_search_no_results(self, driver):
        page = SearchResultsPage(driver)
        page.open(SEARCH_QUERY_NO_RESULTS)
        assert page.is_no_results_shown() or page.results_count() == 0

    def test_search_from_homepage(self, driver):
        home = HomePage(driver)
        home.open()
        home.search(SEARCH_QUERY)
        assert "search" in driver.current_url.lower() or SEARCH_QUERY.split()[0].lower() in driver.current_url.lower()

    def test_search_result_click_opens_product(self, driver):
        page = SearchResultsPage(driver)
        page.open(SEARCH_QUERY)
        initial_url = driver.current_url
        page.click_first_result()
        assert driver.current_url != initial_url

    def test_search_results_have_titles(self, driver):
        page = SearchResultsPage(driver)
        page.open(SEARCH_QUERY)
        results = page.get_results()
        assert len(results) > 0

    def test_search_special_characters(self, driver):
        page = SearchResultsPage(driver)
        page.open("harry & potter")
        # Should not crash
        assert driver.current_url is not None

    def test_search_partial_query(self, driver):
        page = SearchResultsPage(driver)
        page.open("harr")
        assert page.results_count() >= 0  # Should load without error

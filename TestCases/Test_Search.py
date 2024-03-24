from PageObjects.HomePage import HomePage
from Utilities.Reusable import BaseTest
from TestData.Data import TestSearchData

class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        test_search_valid_product = TestSearchData.valid_product_name
        search_page = home_page.search_for_a_product(test_search_valid_product)
        assert  search_page.display_status_of_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        test_search_invalid_product = TestSearchData.invalid_product_name
        search_page = home_page.search_for_a_product(test_search_invalid_product)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product().__eq__(expected_text)

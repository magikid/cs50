from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest


class TestSearch(BaseSeleniumTest):
    def test_search_redirets_to_page_on_exact_match(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.NAME, "q").send_keys("CSS")
        self.selenium.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
        self.assertEqual(self.selenium.current_url, f"{self.live_server_url}/wiki/CSS")

    def test_search_shows_results_page_on_partial_match(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.NAME, "q").send_keys("ytho")
        self.selenium.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
        self.assertEqual(
            self.selenium.current_url, f"{self.live_server_url}/search?q=ytho"
        )
        self.assert_title_contains("Search Results for ytho")
        self.assert_body_contains("Python")

    def test_search_results_are_links(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.NAME, "q").send_keys("ytho")
        self.selenium.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
        self.assertEqual(
            self.selenium.current_url, f"{self.live_server_url}/search?q=ytho"
        )
        self.selenium.find_element(By.LINK_TEXT, "Python").click()
        self.assertEqual(
            self.selenium.current_url, f"{self.live_server_url}/wiki/Python"
        )

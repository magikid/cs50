from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch(BaseSeleniumTest):
    def test_search_redirets_to_page_on_exact_match(self):
        self.selenium.get(f"{self.live_server_url}/")
        search_box = self.selenium.find_element(By.NAME, "q")
        search_box.send_keys("CSS")
        self.selenium.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
        self.assertEqual(self.selenium.current_url, f"{self.live_server_url}/wiki/CSS")

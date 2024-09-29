from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest


class TestRandom(BaseSeleniumTest):
    def test_random_link_works(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Random Page").click()
        self.assertIn("/wiki/", self.selenium.current_url)

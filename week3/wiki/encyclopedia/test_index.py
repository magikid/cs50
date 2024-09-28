from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest


class TestIndex(BaseSeleniumTest):
    def test_index_has_links(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "CSS").click()
        self.assertEqual(self.selenium.current_url, f"{self.live_server_url}/wiki/CSS")

from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest


class TestEntry(BaseSeleniumTest):
    def test_entry_page_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        title = (
            self.selenium.find_element(By.TAG_NAME, "title")
            .get_attribute("innerHTML")
            .strip()
        )
        self.assertEqual(title, "CSS")

    def test_entry_page_has_content(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        content = self.selenium.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        self.assertIn("CSS", content)
        self.assertIn("h1", content)

    def test_missing_entry_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/doesnotexist")
        title = (
            self.selenium.find_element(By.TAG_NAME, "title")
            .get_attribute("innerHTML")
            .strip()
        )
        self.assertIn("doesnotexist", title)

    def test_missing_entry_has_message(self):
        page_title = "doesnotexist"
        self.selenium.get(f"{self.live_server_url}/wiki/{page_title}")
        body = self.selenium.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        self.assertIn(f'The requested page "{page_title}" could not be found', body)

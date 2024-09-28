from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_index_has_links(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "CSS").click()
        self.assertEqual(self.selenium.current_url, f"{self.live_server_url}/wiki/CSS")

    def test_entry_page_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        title = self.selenium.find_element(By.TAG_NAME, "title").get_attribute("innerHTML").strip()
        self.assertEqual(title, "CSS")

    def test_entry_page_has_content(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        content = self.selenium.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
        self.assertIn("CSS", content)
        self.assertIn("h1", content)

    def test_missing_entry_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/doesnotexist")
        title = self.selenium.find_element(By.TAG_NAME, "title").get_attribute("innerHTML").strip()
        self.assertIn("doesnotexist", title)

    def test_missing_entry_has_message(self):
        page_title = "doesnotexist"
        self.selenium.get(f"{self.live_server_url}/wiki/{page_title}")
        body = self.selenium.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
        self.assertIn(f"The requested page \"{page_title}\" could not be found", body)


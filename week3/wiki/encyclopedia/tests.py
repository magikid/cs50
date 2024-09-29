# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class BaseSeleniumTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def assert_title_contains(self, other_string):
        title = (
            self.selenium.find_element(By.TAG_NAME, "title")
            .get_attribute("innerHTML")
            .strip()
        )
        self.assertIn(other_string, title)

    def assert_body_contains(self, other_string):
        body = (
            self.selenium.find_element(By.TAG_NAME, "body")
            .get_attribute("innerHTML")
            .strip()
        )
        self.assertIn(other_string, body)

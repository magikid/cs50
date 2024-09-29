from django.test import TestCase

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

    def assertTitleContains(self, otherString):
        title = self.selenium.find_element(By.TAG_NAME, "title").get_attribute("innerHTML").strip()
        self.assertIn(otherString, title)

    def assertBodyContains(self, otherString):
        body = self.selenium.find_element(By.TAG_NAME, "body").get_attribute("innerHTML").strip()
        self.assertIn(otherString, body)

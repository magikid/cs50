from selenium.webdriver.common.by import By
from django.core.files.storage import default_storage

from .tests import BaseSeleniumTest


class TestEntry(BaseSeleniumTest):
    def test_entry_page_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        self.assertTitleContains("CSS")

    def test_entry_page_has_content(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        content = self.selenium.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        self.assertBodyContains("CSS")
        self.assertBodyContains("h1")

    def test_missing_entry_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/doesnotexist")
        self.assertTitleContains("doesnotexist")

    def test_missing_entry_has_message(self):
        page_title = "doesnotexist"
        self.selenium.get(f"{self.live_server_url}/wiki/{page_title}")
        self.assertBodyContains(f'The requested page "{page_title}" could not be found')

    def test_new_page_form(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").is_displayed()
        self.selenium.find_element(By.NAME, "content").is_displayed()
        self.assertBodyContains("Title")
        self.assertBodyContains("Content")

    def test_new_page_saves_successfully(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").send_keys("foo")
        self.selenium.find_element(By.NAME, "content").send_keys("bar\n# baz")
        self.selenium.find_element(By.CSS_SELECTOR, "#new_entry input[type=submit]").click()
        self.assertBodyContains("foo")
        self.assertBodyContains("<p>bar</p>")
        self.assertBodyContains("<h1>baz</h1>")

        default_storage.delete("entries/foo.md")

    def test_new_page_duplicate_shows_error(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").send_keys("CSS")
        self.selenium.find_element(By.NAME, "content").send_keys("bar\n# baz")
        self.selenium.find_element(By.CSS_SELECTOR, "#new_entry input[type=submit]").click()
        self.assertBodyContains("A page titled CSS already exists.")

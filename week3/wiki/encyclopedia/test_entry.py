from django.core.files.storage import default_storage
from selenium.webdriver.common.by import By

from .tests import BaseSeleniumTest


class TestEntry(BaseSeleniumTest):
    def test_entry_page_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        self.assert_title_contains("CSS")

    def test_entry_page_has_content(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        self.assert_body_contains("CSS")
        self.assert_body_contains("h1")

    def test_missing_entry_sets_title(self):
        self.selenium.get(f"{self.live_server_url}/wiki/doesnotexist")
        self.assert_title_contains("doesnotexist")

    def test_missing_entry_has_message(self):
        page_title = "doesnotexist"
        self.selenium.get(f"{self.live_server_url}/wiki/{page_title}")
        self.assert_body_contains(
            f'The requested page "{page_title}" could not be found'
        )

    def test_new_page_form(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").is_displayed()
        self.selenium.find_element(By.NAME, "content").is_displayed()
        self.assert_body_contains("Title")
        self.assert_body_contains("Content")

    def test_new_page_saves_successfully(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").send_keys("foo")
        self.selenium.find_element(By.NAME, "content").send_keys("bar\n# baz")
        self.selenium.find_element(
            By.CSS_SELECTOR, "#new_entry input[type=submit]"
        ).click()
        self.assert_body_contains("foo")
        self.assert_body_contains("<p>bar</p>")
        self.assert_body_contains("<h1>baz</h1>")

        default_storage.delete("entries/foo.md")

    def test_new_page_duplicate_shows_error(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.find_element(By.LINK_TEXT, "Create New Page").click()
        self.selenium.find_element(By.NAME, "title").send_keys("CSS")
        self.selenium.find_element(By.NAME, "content").send_keys("bar\n# baz")
        self.selenium.find_element(
            By.CSS_SELECTOR, "#new_entry input[type=submit]"
        ).click()
        self.assert_body_contains("A page titled CSS already exists.")

    def test_edit_page(self):
        self.selenium.get(f"{self.live_server_url}/wiki/CSS")
        self.selenium.find_element(By.LINK_TEXT, "Edit entry").click()
        textarea = self.selenium.find_element(By.TAG_NAME, "textarea")
        self.assertIn(
            "CSS is a language that can be used to add style to an",
            textarea.get_attribute("value").strip(),
        )
        textarea.send_keys("test test test")
        self.selenium.find_element(
            By.CSS_SELECTOR, "#edit_entry input[type=submit]"
        ).click()
        self.assert_body_contains("test test test")

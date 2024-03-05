from page_objects.base_page import BasePage


class GooglePage(BasePage):
    search_box = '[name="q"]'

    def test_search(self, search):
        self.type(self.search_box, search)
        self.page.keyboard.press("Enter")
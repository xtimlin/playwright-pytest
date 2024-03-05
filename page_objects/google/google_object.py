from page_objects.base_page import BasePage


class GooglePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_box = self.page.locator('[name="q"]')

    def test_search(self, search):
        self.search_box.fill(search)
        self.search_box.press("Enter")
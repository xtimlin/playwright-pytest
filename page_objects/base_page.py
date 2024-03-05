from playwright.async_api import Page
from playwright.sync_api import TimeoutError as TError


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.click(locator)

    def check(self, locator: str):
        self.page.check(locator)

    def uncheck(self, locator: str):
        self.page.check(locator)

    def hover(self, locator: str):
        self.page.hover(locator)

    def go_to_url(self, url: str):
        self.page.goto(url)

    def type(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    def select_option(self, locator: str, option: str):
        self.page.selectOption(locator, option)

    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.waitForSelector(locator)
            return True
        except TError:
            return False

    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.waitForSelector(locator, state='hidden')
            return True
        except TError:
            return False

import time
import pytest
import unittest


class TestAmazon(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def initialize_browser(self, playwright_browser):
        self.page = playwright_browser
        # self.pd_page_object = AmazonPage(self.page)

    def test_amazon(self):
        """
        1. Navigate to the Amazon home page
        2. Click the left side navigation and select Amazon prime button
        3. Click the Amazon prime option
        4. Verify the user is able to land on the prime video page
        """
        self.page.goto('https://www.amazon.com/')
        time.sleep(10)
        self.page.click("[id='nav-hamburger-menu']")
        self.page.click("//*[@id='hmenu-content']/ul[1]/li[8]/a")
        self.page.click("//*[@id='hmenu-content']/ul[3]/li[3]/a")
        assert self.page.locator('//*[@id="pv-nav-container"]/div/a/img').is_visible()

        time.sleep(60)

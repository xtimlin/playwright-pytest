import time
import pytest
import unittest
from page_objects.duckduckgo.duckduckgo_object import DuckduckgoPage


class TestDuckduckgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # setup data
        pass

    @classmethod
    def tearDownClass(cls):
        # clean data
        pass

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    @pytest.fixture(autouse=True)
    def initialize_browser(self, playwright_browser):
        self.page = playwright_browser
        self.driver = DuckduckgoPage(self.page)
        self.driver.go_to_url('https://duckduckgo.com/')

    def test_duckduckgo_search_playwright(self):
        self.driver.test_search('playwright')
        time.sleep(1)

    def test_duckduckgo_search_selenium(self):
        self.driver.test_search('selenium')
        time.sleep(1)

import time
import pytest
import unittest
from page_objects.google.google_object import GooglePage


class TestGoogle(unittest.TestCase):

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
        self.driver = GooglePage(self.page)
        self.driver.go_to_url('https://google.com/')

    def test_google_search_playwright(self):
        self.driver.test_search('playwright')
        time.sleep(1)

    def test_google_search_selenium(self):
        self.driver.test_search('selenium')
        time.sleep(1)

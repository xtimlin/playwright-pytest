import time
import pytest
import unittest
from page_objects.prescriptive_data.prescriptive_data_object import PrescriptiveDataPage


class TestPrescriptiveData(unittest.TestCase):

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
        self.pd_page_object = PrescriptiveDataPage(self.page)

    def test_PD_schedule_demo(self):
        details = {
            'firstname': 'test firstname',
            'lastname': 'test lastname',
            'email': 'test@email.com',
            'company': 'test company',
            'jobTitle': 'test jobTitle',
            'frimType': 'Brokerage',
        }
        self.pd_page_object.go_to_schedule_demo_page()
        self.pd_page_object.filling_schedule_demo_form(details)
        time.sleep(2)

        # verify data in DB or API
import unittest
import pytest
from apis.base_api import BaseAPI
from apis.routes import routes


class TestFakerestAPI(unittest.TestCase):
    # https://fakerestapi.azurewebsites.net/index.html
    # https://fakerestapi.azurewebsites.net/api/v1/Activities


    def setUp(self):
        self.obj = BaseAPI('https://fakerestapi.azurewebsites.net/')

    def test_Fakerest_API_test(self):
        response = self.obj.api('get', 'api/v1/Activities', None)
        assert response.status_code == 200
        response = response.json()
        assert response is not None
        assert len(response) > 0
        complete = 0
        incomplete = 0
        for item in response:
            if item['completed'] == True:
                complete += 1
            else:
                incomplete += 1

        print('complete: ' + str(complete))
        print('incomplete: ' + str(incomplete))

import unittest
import pytest
from apis.base_api import BaseAPI
from apis.routes import routes

from data.reqres_data import data


class TestReqresAPI(unittest.TestCase):
    # https://reqres.in/

    @classmethod
    def setUpClass(cls):
        # setup data
        pass

    @classmethod
    def tearDownClass(cls):
        # clean data
        pass

    def setUp(self):
        self.obj = BaseAPI('https://reqres.in/')

    def test_users(self):
        response = self.obj.api('get', routes['users'], None)
        assert response.status_code == 200
        response = response.json()
        assert response['data'] is not None

    def test_get_user_by_id(self):
        response = self.obj.api('get', routes['get_user'].format(1), None)
        assert response.status_code == 200
        response = response.json()
        assert response['data'] is not None
        print(response)

    def test_create_user(self):
        body = data['create_user']
        response = self.obj.api('post', routes['get_user'], body)
        assert response.status_code == 201
        response = response.json()
        assert response is not None
        assert response['name'] == body["name"]
        assert response['job'] == body["job"]
        assert response['id'] is not None
        print(response)
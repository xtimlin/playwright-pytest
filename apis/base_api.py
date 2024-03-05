import json
import requests


class BaseAPI:
    def __init__(self, base_url=None):
        self.api_base_url = base_url

    def api(
            self,
            method,
            end_point,
            body,
            base_url=None,
            header=None,
            auth=None,
    ):
        if not header:
            header = {"Content-Type": "application/json"}
        if auth:
            header["Authorization"] = "Bearer {}".format(auth)
        if not base_url:
            base_url = self.api_base_url
        header["User-Agent"] = "automation tester"
        url = base_url + end_point
        response = ""
        if method == "get":
            response = requests.get(url, params=body, headers=header)
        if method == "post":
            response = requests.post(url, data=json.dumps(body), headers=header)
        if method == "put":
            response = requests.put(url, data=json.dumps(body), headers=header)
        if method == "delete":
            response = requests.delete(url, data=json.dumps(body), headers=header)
        if method == "patch":
            requests.patch(url, data=json.dumps(body), headers=header)

        return response

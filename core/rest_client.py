import json

import requests

from utils.log_util import logger
from utils.read import base_data

api_root_url_get = base_data.read_ini_host()['host']['api_test_url_get']
api_root_url_post = base_data.read_ini_host()['host']['api_test_url_post']


class RestClient:
    def __init__(self):
        self.api_root_url_get = api_root_url_get
        self.api_root_url_post = api_root_url_post
        self.session = requests.session()

    def get(self, url, **kwargs):
        # return requests.get(self.api_root_url + url, **kwargs)
        return self.request(url, "GET", **kwargs)

    def post(self, url, **kwargs):
        # return requests.post(self.api_root_url + url, **kwargs)
        return self.request(url, "POST", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, "PUT", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == "GET":
            return self.session.get(self.api_root_url_get + url, **kwargs)
        if method == "POST":
            return self.session.post(self.api_root_url_post + url, **kwargs)
        # if method == "PUT":
        #     return requests.put(self.api_root_url + url, **kwargs)
        # if method == "DELETE":
        #     return requests.delete(self.api_root_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        data = dict(**kwargs).get("data")
        headers = dict(**kwargs).get("headers")
        logger.info("接口请求的方法>>>{}".format(method))
        if method == "GET":
            logger.info("接口请求的地址>>>{}".format(self.api_root_url_get + url))
        if method == "POST":
            logger.info("接口请求的地址>>>{}".format(self.api_root_url_post + url))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, indent=2)))
        if headers is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(headers, indent=2)))
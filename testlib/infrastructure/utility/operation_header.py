# coding: utf-8
import json


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_url(self):
        '''
        获取登录返回的token的url
        '''
        url = self.response['data']['url'][0]
        return url

    def get_cookie(self):
        pass

    def write_cookie(self):
        pass


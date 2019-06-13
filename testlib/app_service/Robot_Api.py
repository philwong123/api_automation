#encoding: utf-8
from testlib.infrastructure.common.get_data import GetData

class Robot_Api(object):
    def __init__(self):
        self.data = GetData()
    
    def get_case_num(self):
        return self.data.get_case_lines()

    def form_data(self, i):
        request_data = self.data.get_request_data(i)
        url = self.data.get_request_url(i)
        request_data['url'] = url
        method = self.data.get_request_method(i)
        request_data['method'] = method
        token = self.data.get_token(i)
        request_data['token'] = token
        return request_data
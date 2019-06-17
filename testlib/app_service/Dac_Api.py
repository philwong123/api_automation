# -*- coding: utf-8 -*-
import requests
import json
from testlib.infrastructure.common.get_data import GetData


class Dac_Api(object):

    def post(self, url, data, header=None):
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res
 
    def get(self, url, data=None, header=None):
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res
 
    def run(self, method, url, data=None, header=None):
        if method == 'POST':
            res = self.post(url,data,header)
        else:
            res = self.get(url,data,header)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=3)
        return res
 
    @staticmethod
    def form_request_data():
        data = GetData()
        for i in range(1, 5):
            url = data.get_request_url(i)
            method = data.get_request_method(i)
            request_data = data.get_request_data(i)
            token = data.get_token(i)
            expect = data.get_expcet_data(i)
            request_data['token'] = token
        return request_data
 
    @staticmethod
    def robot_post():
        data = GetData()
        url = data.get_request_url(1)
        data = Dac_Api.form_request_data()
        print ('data',data)
        response = requests.post(url=url)
        res = json.loads(response.content)
        print('rebot_post_res',res, "\n",type(res), response.status_code)
        return response.status_code
#         return res["returnCode"]
# 
if __name__ == '__main__':
    dacApi = Dac_Api()
#     data = GetData()
#     for i in range(1,5):
#         url = data.get_request_url(i)
#         method = data.get_request_method(i)
#         request_data = data.get_data_from_json(i)
#         token = data.get_token(i)
#         expect = data.get_expcet_data(i)
#         request_data['token'] = token
#         res = dacApi.post(url, data=request_data)
#         print('post result: ', res,res.content)
    Dac_Api.robot_post()
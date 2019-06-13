#coding: utf-8
import requests
from testlib.app_service.Dac_Api import Dac_Api
from testlib.infrastructure.common.get_data import GetData


class RunTest:
    def __init__(self):
        self.run_method = Dac_Api()
        self.data = GetData()

    def run_test(self):
        res = None
        pass_count = []
        fail_count = []
        #10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(i)
                token = self.data.get_token(i)
                request_data['token'] = token
                expect = self.data.get_expcet_data(i)
                res = self.run_method.run(method, url, request_data)
                print ("res is ",res.content,type(res.content))
#                 if self.compare_dict.check_return_code(res.content, expect):
#                     self.data.write_result(i,'pass')
#                     pass_count.append(i)
#                 else:
#                     self.data.write_result(i,res)
#                     fail_count.append(i)

if __name__ == '__main__':
    run = RunTest()
    run.run_test()
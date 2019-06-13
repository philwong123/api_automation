#encoding: utf-8
import os
import sys
import allure
import pytest
import logging
from testlib.app_service.send_request import Send_Request
import testlib.infrastructure.common.constants as Consts
from testlib.infrastructure.common.assertion import Assertions
from testlib.infrastructure.common.get_data import GetData

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data = GetData()


class TestDAC(object):

    @allure.step("reponse")
    # 测试步骤，打印返回信息
    def print_message(self, url, request_data):
        request = Send_Request()
        response = request.post_request(url, data=request_data)
        logging.info("RESPONSE: {}".format(response['body']))
        return response

    #作用于class用例集中的用例，置于class内，只在class用例执行的开始执行setup_class,结束时执行teardown_class
    def setup_class(self):
        logging.info("do something before class!")

    def teardown_class(self):
        logging.info("do something after class!")

    #仅作用于class用例集中的用例，置于class内,每个用例都会调用一次setup_method, teardown_method
    # def setup_method(self):
    #     logging.info("do something before test!")
    #
    # def teardown_method(self):
    #     logging.info("do something after test!")


    @pytest.allure.feature('DAC_demo1')
    @allure.severity('Critical')
    @allure.story('test_srory_1')
    def test_dac_01(self):

        """
        用例描述：1. 获取所有设备实时信息
        """
        case_id = "DAC_01"
        logging.info("START TEST CASE: {}".format(case_id))
        test = Assertions()
        request = Send_Request()
        row = data.get_row_by_id(case_id)
        is_run = data.get_is_run(row)
        if is_run:
            url = data.get_request_url(row)
            request_data = data.get_request_data(row)
            token = data.get_token(row)
            request_data['token'] = token

        response = self.print_message(url, request_data)
        assert test.assert_code(response['body']['returnCode'], '200')
        assert test.assert_time(response['time_consuming'], 500)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC_demo2')
    @allure.severity('Normal')
    @allure.story('test_story_2')
    def test_dac_02(self):
        """
        用例描述：2. 获取所有设备历史信息
        """
        case_id = "DAC_02"
        logging.info("START TEST CASE: {}".format(case_id))
        test = Assertions()
        request = Send_Request()
        row = data.get_row_by_id(case_id)
        is_run = data.get_is_run(row)
        if is_run:
            url = data.get_request_url(row)
            request_data = data.get_request_data(row)
            token = data.get_token(row)
            request_data['token'] = token

        response = self.print_message(url, request_data)
        assert test.assert_code(response['body']['returnCode'], '200')
        assert test.assert_time(response['time_consuming'], 500)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC_demo3')
    @allure.severity('Blocker')
    @allure.story('test_story_3')
    def test_dac_03(self):
        """
        用例描述：3. 获取设备的时长信息
        """
        case_id = "DAC_03"
        logging.info("START TEST CASE: {}".format(case_id))
        test = Assertions()
        request = Send_Request()
        row = data.get_row_by_id(case_id)
        is_run = data.get_is_run(row)
        if is_run:
            url = data.get_request_url(row)
            request_data = data.get_request_data(row)
            token = data.get_token(row)
            request_data['token'] = token

        response = self.print_message(url, request_data)
        assert test.assert_code(response['body']['returnCode'], '200')
        assert test.assert_time(response['time_consuming'], 1500)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC_demo1')
    @allure.severity('Blocker')
    @allure.story('test_story_4')
    def test_dac_04(self):
        """
        用例描述：4. 获取所有设备的产量
        """
        case_id = "DAC_04"
        logging.info("START TEST CASE: {}".format(case_id))
        test = Assertions()
        request = Send_Request()
        row = data.get_row_by_id(case_id)
        is_run = data.get_is_run(row)
        if is_run:
            url = data.get_request_url(row)
            request_data = data.get_request_data(row)
            token = data.get_token(row)
            request_data['token'] = token

        response = self.print_message(url, request_data)
        assert test.assert_code(response['body']['returnCode'], '200')
        assert test.assert_time(response['time_consuming'], 500)
        Consts.RESULT_LIST.append('True')
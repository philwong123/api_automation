# -*- coding: utf-8 -*-
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


    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('实时数据接口')
    def test_dac_01(self):

        """
        用例描述：1. 获取实时数据，"app": "1"
        """
        case_id = "实时数据"
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

    @pytest.allure.feature('DAC接口')
    @allure.severity('Block')
    @allure.story('历史数据接口')
    def test_dac_02(self):
        """
        用例描述：2. 获取所有设备历史信息，根据用户传入的token，采集参数，时间段以及设备编号获取该时间段内该设备采集参数的所有采集记录
        "app": "2"
        """
        case_id = "历史数据"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('设备信息表')
    def test_dac_03(self):
        """
        用例描述：3. 获取所有设备的信息，"app": "12"
        """
        case_id = "设备信息表"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('网关信息表')
    def test_dac_04(self):
        """
        用例描述：4. 获取网关信息表，"app": "13"
        """
        case_id = "网关信息表"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('告警数据接口')
    def test_dac_05(self):
        """
        用例描述：5. 获取告警数据,"app": "66"
        """
        case_id = "告警数据"
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
        assert test.assert_value_not_null(response['body']['Values'])
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('变量信息表')
    def test_dac_06(self):
        """
        用例描述：6. 获取变量信息表, "app": "15"
        """
        case_id = "变量信息表"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('单台设备实时信息')
    def test_dac_07(self):
        """
        用例描述：7. 获取单台设备实时信息, "app": "16"
        """
        case_id = "单台设备实时信息"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('单台设备的信息')
    def test_dac_08(self):
        """
        用例描述：8. 获取单台设备的信息,"app": "25"
        """
        case_id = "单台设备的信息"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('设备产量')
    def test_dac_09(self):
        """
        用例描述：9. 获取设备产量,"app": "23"
        """
        case_id = "设备产量"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('机器人寻位、焊接状态信息')
    def test_dac_10(self):
        """
        用例描述：10. 获取机器人寻位、焊接状态信息, /get/robotStatus/
        """
        case_id = "机器人寻位、焊接状态信息"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('极大，极小，平均值')
    def test_dac_11(self):
        """
        用例描述：11. 获取极大，极小，平均值
        """
        case_id = "极大，极小，平均值"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('获取历史数据')
    def test_dac_12(self):
        """
        用例描述：12. 获取机器人寻位、焊接状态信息
        """
        case_id = "获取历史数据"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('获取所有设备信息')
    def test_dac_13(self):
        """
        用例描述：13. 获取所有设备信息
        """
        case_id = "获取所有设备信息"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('设备时间状态统计')
    def test_dac_14(self):
        """
        用例描述：14. 获取设备时间状态统计
        """
        case_id = "设备时间状态统计"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('设备状态判断的公式')
    def test_dac_15(self):
        """
        用例描述：15. 设备状态判断的公式
        """
        case_id = "设备状态判断的公式"
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
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('DAC接口')
    @allure.severity('Critical')
    @allure.story('返回该公司所有设备数据')
    def test_dac_16(self):
        """
        用例描述：16. 返回该公司所有设备数据
        """
        case_id = "返回该公司所有设备数据"
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
        Consts.RESULT_LIST.append('True')
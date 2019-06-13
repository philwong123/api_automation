#encoding: utf-8
import json
import logging
from testlib.infrastructure.log.test_log import TestLog
from testlib.infrastructure.common import constants as Consts


class Assertions(object):
    def __init__(self):
        # self.log = TestLog()
        pass

    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            return True
        except:
            logging.error("statusCode error, expected_code is {}, statusCode is {} ".format(expected_code, code))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            logging.error("Response body msg != expected_msg, expected_msg is {}, body_msg is {}".format(expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True
        except:
            logging.error("Response body Does not contain expected_msg, expected_msg is {}".format(expected_msg))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True
        except:
            logging.error("Response body != expected_msg, expected_msg is {}, body is {}".format(expected_msg, body))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True
        except:
            logging.error("Response time > expected_time, expected_time is {}, time is {}" .format(expected_time, time))
            Consts.RESULT_LIST.append('fail')
            raise
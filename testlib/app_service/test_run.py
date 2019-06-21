# -*- coding: utf-8 -*-
import sys
import pytest
import logging
from testlib.infrastructure.log.test_log import TestLog
from testlib.infrastructure.common.read_config import ReadConfig
from testlib.infrastructure.common.shell import Shell
from testlib.infrastructure.common.send_mail import SendMail
"""
运行用例集：
    python3 test_run.py

# '--allure_severities=critical, blocker, normal'
# '--allure_stories=test_demo1, test_demo2'
# '--allure_features=test features'
"""



if __name__ == '__main__':
    log = TestLog()
    config = ReadConfig()
    shell = Shell()
    logging.info('初始化配置文件')
    path = config.get_project_path("project_path")
    xml_report_path = path + "/Report/xml"
    html_report_path = path + "/Report/html"
    # 定义测试集
    allure_list = '--allure_features=DAC'
    # args = ['-s', '-q', r'D:\demo\testlib\case', '--alluredir', xml_report_path, allure_list]
    args = ['-s', '-q', r'D:\twinkle\testlib\case', '--alluredir', xml_report_path]
    logging.info('执行用例集为：{}'.format(allure_list))
    self_args = sys.argv[1:]
    # 执行测试用例
    pytest.main(args)

    #生成报告
    cmd = 'allure generate {0} -o {1} --clean'.format(xml_report_path, html_report_path)
    print(cmd)
    shell.invoke(cmd)
    logging.info('生成报告成功')

    # mail = SendMail()
    # mail.send_mail()
    # logging.info('测试完成')
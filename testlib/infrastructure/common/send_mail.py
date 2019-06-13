# -*- coding: utf-8 -*-
# @Time    : 2019/6/11
# @Author  : Wang Ye
# @File    : send_mail.py
import smtplib
import time
import logging
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import testlib.infrastructure.common.constants as Consts
from testlib.infrastructure.common.read_config import ReadConfig


class SendMail(object):

    def __init__(self):
        self.config = ReadConfig()

    def send_mail(self):
        msg = self._form_mail_msg()
        receiver = self.config.get_email('receiver')
        receivers = receiver.split(',')
        msg['To'] = ",".join(receivers)
        username = self.config.get_email('mail_user')
        password = self.config.get_email('mail_pass')
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.get_email('mail_host'))
            smtp.login(username, password)
            smtp.sendmail(self.config.get_email('sender'), receivers, msg.as_string())
        except Exception as e:
            logging.error(e)
            logging.error("发送失败")
            logging.error("邮件发送失败，请检查邮件配置")

        else:
            logging.info("发送成功")
            logging.info("邮件发送成功")
        finally:
            smtp.quit()

    def _form_mail_msg(self):
        msg = MIMEMultipart()
        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        body = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：{0}\n   接口运行结果集：{1}'.format(stress_body, result_body)
        mail_body = MIMEText(body, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        msg['From'] = self.config.get_email('sender')
        receiver = self.config.get_email('receiver')
        receivers = receiver.split(',')
        msg['To'] = ",".join(receivers)
        msg.attach(mail_body)
        return msg
# -*- coding: utf-8 -*-
import os
import random
import requests
import testlib.infrastructure.common.constants as Consts


class Send_Request(object):

    def __init__(self):
        pass

    def get_request(self, url, data, header):
        try:
            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
        except Exception as e:
            print(e)
        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request(self, url, data, header=None):
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                response = requests.post(url=url, data=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
        except Exception as e:
            print(e)

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

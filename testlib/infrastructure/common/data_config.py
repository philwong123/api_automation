# coding: utf-8

class GlobalVar(object):
    #case_id
    Id = '0'
    api_name = '1'
    url = '2'
    token = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
    run = '12'

    @staticmethod
    def get_id():
        return GlobalVar.Id

    @staticmethod
    def get_api_name():
        return GlobalVar.api_name

    @staticmethod
    def get_url():
        return GlobalVar.url

    @staticmethod
    def get_token():
        return GlobalVar.token

    @staticmethod
    def get_run():
        return GlobalVar.run

    @staticmethod
    def get_run_way():
        return GlobalVar.request_way

    @staticmethod
    def get_header():
        return GlobalVar.header

    @staticmethod
    def get_case_depend():
        return GlobalVar.case_depend

    @staticmethod
    def get_data_depend():
        return GlobalVar.data_depend

    @staticmethod
    def get_field_depend():
        return GlobalVar.field_depend

    @staticmethod
    def get_data():
        return GlobalVar.data

    @staticmethod
    def get_expect():
        return GlobalVar.expect

    @staticmethod
    def get_result():
        return GlobalVar.result

    @staticmethod
    def get_header_value():
        return GlobalVar.header
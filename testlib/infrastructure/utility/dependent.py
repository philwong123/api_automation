#coding: utf-8


class DependentData(object):
    def __init__(self,case_id):
        self.case_id = case_id

    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        pass

    #执行依赖测试，获取结果
    def run_dependent(self):
        pass

    #根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_from_key(self,row):
        pass

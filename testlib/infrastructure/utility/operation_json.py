# coding: utf-8
import json


class OperationJson(object):

    def __init__(self, file_path=None):
        if file_path  == None:
            self.file_path = 'D:/demo/testlib/dataconfig/default.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path, 'r') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        if id in self.data:
            return self.data
        else:
            return None

    #写json
    def write_data(self,data):
        with open('D:/demo/dataconfig/cookie.json','w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_post_data('app'))
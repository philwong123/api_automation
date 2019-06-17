# coding： utf-8
import subprocess


class Shell:

    @staticmethod
    def invoke(cmd):
        try:
            output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            output = output.decode(encoding='gb2312')
        except Exception as e:
            print(e)
        return output

if __name__ =="__main__":
    s = Shell()
    o = s.invoke('allure generate D:\\demo\\testlib\\Report\\xml -o D:\\demo\\testlib\\Report\\html --clean')
    # o = s.invoke('ping www.baidu.com')
    print (o)
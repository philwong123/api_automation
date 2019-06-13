#coding: utf-8
import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
proDir = os.path.abspath(os.path.join(proDir, "../.."))
configPath = os.path.join(proDir, r"dataconfig/config.ini")


class ReadConfig(object):
    def __init__(self):
        fd = open(configPath, 'r')
        data = fd.read()
        self.cfg = configparser.ConfigParser()
        self.cfg.read(configPath)
    
    def get_case_path(self, name):
        value = self.cfg.get("COMMON", name)
        return value

    def get_project_path(self, name):
        return self.cfg.get("COMMON", name)

    def get_email(self, name):
        value = self.cfg.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cfg.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cfg.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cfg.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cfg.write(f)

    def get_url(self, name):
        value = self.cfg.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cfg.get("DATABASE", name)
        return value


if __name__ == "__main__":
    rc = ReadConfig()
    print(rc.get_case_path("case_path"))
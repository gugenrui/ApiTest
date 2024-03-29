import yaml
import os
import configparser

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "file", "update.png")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "setting.ini")


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path
        self.file_path = file_path

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        return data

    def read_ini_host(self):
        config = configparser.ConfigParser()  # 实例化对象
        config.read(self.ini_path, encoding='utf8')
        return config

    def read_file(self):
        f = open(self.file_path, 'rb')
        return {'file': ('update.png', f, 'image/png')}


base_data = FileRead()

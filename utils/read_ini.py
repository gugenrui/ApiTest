import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "setting.ini")


def read_ini_host():
    config = configparser.ConfigParser()  # 实例化对象
    config.read(path, encoding="utf8")
    return config

get_ini = read_ini_host()
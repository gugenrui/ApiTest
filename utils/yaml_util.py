# 随机名字输出
from faker import Faker
import random

fake = Faker(locale="zh-CN")


def func_yaml_person(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if '${' and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                func_name = str(value)[start + 2:end]
                data[key] = str(value)[0:start] + str(eval(func_name)) + str(value)[end + 1:len(str(value))]
    return data


def random_name():
    return fake.name()


def age():
    return random.randint(22, 120)


def sex():
    return random.choice(["男", "女", "变态"])


if __name__ == '__main__':
    data = {'name': '南京-${random_name()}-测试', 'age': '${age()}', 'sex': '${sex()}'}
    print(func_yaml_person(data))

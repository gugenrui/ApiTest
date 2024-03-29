import yaml
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml")


def read_data():
    f = open(path, encoding="utf8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()
print(get_data)
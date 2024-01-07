from utils.read_data_test import get_data
from utils import yaml_util
import pytest


@pytest.mark.parametrize("data", get_data["person"])
def test_person(data):
    res = yaml_util.func_yaml_person(data)
    print(res)
    assert type(res["name"]) == str
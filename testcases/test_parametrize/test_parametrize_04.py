import pytest

from utils.read_data_test import get_data, read_data


# 单参数
# @pytest.mark.parametrize("name", get_data['heros_name'])
# def test_parametrize_03(name):
#     print(name)

# 多参数
@pytest.mark.parametrize("name, line", get_data['heros_name_word'])
def test_parametrize_03(name, line):
    print('%s的台词是"%s"' % (name, line))

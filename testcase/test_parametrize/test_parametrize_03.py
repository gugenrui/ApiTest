import pytest

# 参数值为字典
from utils.read_data_test import get_data


@pytest.mark.parametrize("hero", get_data["heros"])
def test_parametrize_03(hero):
    print(hero)
    # print(f'{name}的台词是"{word}"')
    print("%s的台词是%s" % (hero["name"], hero["word"]))

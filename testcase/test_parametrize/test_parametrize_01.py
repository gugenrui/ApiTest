import pytest


# 单参数单次循环
# @pytest.mark.parametrize("name", ["grey_gu"])
# def test_parametrize(name):
#     print("I am " + name)


# 单参数多次循环
# 运行时，将数组里的值分别赋值给变量，每赋值一次，运行一次
@pytest.mark.parametrize("name", ["李白", "孙尚香", "鲁班", "安其拉"])
def test_parametrize(name):
    print("pass")

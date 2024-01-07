# 1.登录 2.查找商品 3.下单 4.支付
import pytest
@pytest.mark.run(order=1)
def test_login():
    print("login...")

@pytest.mark.run(order=4)
def test_pay():
    print("pay...")

@pytest.mark.run(order=2)
def test_search():
    print("search...")

@pytest.mark.run(order=3)
def test_order():
    print("order...")
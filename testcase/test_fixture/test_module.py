import requests
import pytest


# 默认scope是function
@pytest.fixture(scope="module", autouse=True)
def function():
    print("我是前置步骤~")

class TestClassFixture:
    def test_mobile_get(self):
        params = {
            "shouji": "15705187072",
            "appkey": "0c818521d38759e1"
        }
        r = requests.get(url="http://api.binstd.com/shouji/query", params=params)
        assert r.status_code == 200
        print(r.status_code)
        result = r.json()
        assert result['status'] == 0
        assert result['result']['company'] == '中国移动'


    def test_mobile_post(self):
        params = {
            "shouji": "15705187072",
            "appkey": "0c818521d38759e1"
        }
        r = requests.post(url="http://api.binstd.com/shouji/query", params=params)
        assert r.status_code == 200
        print(r.status_code)
        result = r.json()
        assert result['status'] == 0
        assert result['result']['company'] == '中国移动'

def test_mobile_post():
    params = {
        "shouji": "15705187072",
        "appkey": "0c818521d38759e1"
    }
    r = requests.post(url="http://api.binstd.com/shouji/query", params=params)
    assert r.status_code == 200
    print(r.status_code)
    result = r.json()
    assert result['status'] == 0
    assert result['result']['company'] == '中国移动'

if __name__ == '__main__':
    pytest.main()
import requests
import pytest

from utils.read_data_test import get_data
from utils.read_ini import get_ini

url = get_ini['host']['api_test_url']
print(url)


@pytest.mark.parametrize("param", get_data["mobile_belong_get"])
def test_mobile_get(param):
    print(param)
    r = requests.get(url=url + "/shouji/query", params=param)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['result']['company'] == '中国移动'


@pytest.mark.parametrize("mobile, appkey", get_data["mobile_belong_post"])
def test_mobile_post(mobile, appkey):
    params = {
        "shouji": mobile,
        "appkey": appkey
    }
    r = requests.post(url=url + "/shouji/query", params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['result']['company'] == '中国移动'


if __name__ == '__main__':
    pytest.main()

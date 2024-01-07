import requests
import pytest

from utils.read import base_data

get_data = base_data.read_data()
url = base_data.read_ini_host()['host']['api_test_url']


@pytest.mark.parametrize("param", get_data["mobile_belong_get"])
def test_mobile_get(param):
    print(param)
    r = requests.get(url=url + "/shouji/query", params=param)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['result']['company'] == '中国移动'


if __name__ == '__main__':
    pytest.main()

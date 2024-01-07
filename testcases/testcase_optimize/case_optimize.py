import pytest

from api.api import mobile_query
from utils.read import base_data

get_data = base_data.read_data()
url = base_data.read_ini_host()['host']['api_test_url']


@pytest.mark.parametrize("params", get_data["mobile_belong_get"])
def test_mobile_get(params):
    result = mobile_query(params)
    assert result['status'] == 0
    assert result['result']['company'] == '中国移动'



if __name__ == '__main__':
    pytest.main()

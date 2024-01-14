import requests
import pytest

@pytest.mark.ggr
class TestMobile:
    def setup_class(self):
        print('准备测试数据')

    def teardown_class(self):
        print('清理测试数据')

    def test_mobile_get(self):
        params = {
            "shouji": "15705187072",
            "appkey": "0c818521d38759e1"
        }
        r = requests.get(url="http://api.binstd.com/shouji/query", params=params)
        assert r.status_code == 200
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
        result = r.json()
        assert result['status'] == 0
        assert result['result']['company'] == '中国移动'


if __name__ == '__main__':
    pytest.main()

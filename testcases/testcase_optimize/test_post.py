import pytest

from api.api import mobile_json
from utils.read import base_data

get_data = base_data.read_data()


def test_post():
    json_data = base_data.read_data()["json_data"]
    result = mobile_json(json_data)
    assert result["id"] == 101


if __name__ == '__main__':
    pytest.main()

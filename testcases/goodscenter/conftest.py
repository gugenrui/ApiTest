# 商品中心conftest
import pytest

from utils.mysql_util import db


# 查询banner数量
@pytest.fixture()
def get_banner_count():
    sql = "SELECT COUNT(*) AS banner_num FROM goods_banner;"
    result = db.select_db_one(sql)
    return result['banner_num']


if __name__ == '__main__':
    get_banner_count()
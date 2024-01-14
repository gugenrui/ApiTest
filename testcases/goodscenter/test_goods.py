import allure

from api.goods_api import get_banner
from testcases.goodscenter.conftest import get_banner_count


@allure.feature("商品中心模块")
class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner测试用例")
    def test_banner(self, get_banner_count):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == get_banner_count

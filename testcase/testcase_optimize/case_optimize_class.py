import allure
import pytest

from api.api import mobile_query
from utils.read import base_data

get_data = base_data.read_data()

@allure.epic("数据进制项目epic")
@allure.feature("手机号模块feature")
class TestMobile:
    @allure.story("杭州的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https//www.baidu.com", name="接口地址testcase")
    @allure.issue("https//www.baidu.com", name="缺陷地址issue")
    @allure.description("当前手机号是13456755448，归属地是杭州的描述")
    @allure.step("先进性归属地的操作step")
    @allure.severity(severity_level="blocker")
    def test_mobile_get(self):
        params = get_data["mobile_belong"]
        result = mobile_query(params)
        assert result.success is True
        assert result.body['status'] == 0
        assert result.body['result']['company'] == '中国移动'

    @allure.story("杭州的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https//www.baidu.com", name="接口地址testcase")
    @allure.issue("https//www.baidu.com", name="缺陷地址issue")
    @allure.description("当前手机号是13456755448，归属地是杭州的描述")
    @allure.step("先进性归属地的操作step")
    @allure.severity(severity_level="blocker")
    def test_mobile_get2(self):
        params = get_data["mobile_belong"]
        result = mobile_query(params)
        assert result.success is True
        assert result.body['status'] == 0
        assert result.body['result']['company'] == '中国移动'

    @allure.story("杭州的手机号story")
    @allure.title("测试手机号归属地title")
    @allure.testcase("https//www.baidu.com", name="接口地址testcase")
    @allure.issue("https//www.baidu.com", name="缺陷地址issue")
    @allure.description("当前手机号是13456755448，归属地是杭州的描述")
    @allure.step("先进性归属地的操作step")
    @allure.severity(severity_level="blocker")
    def test_mobile_get3(self):
        params = get_data["mobile_belong"]
        result = mobile_query(params)
        assert result.success is True
        assert result.body['status'] == 0
        assert result.body['result']['company'] == '中国移动11'


if __name__ == '__main__':
    pytest.main()

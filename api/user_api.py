from core.api_util import api_util
from utils.response_utils import process_response


def send_code(json_data):
    """
    获取短信验证码
    :param json_data:
    :return:
    """
    response = api_util.get_code(json=json_data)
    return process_response(response)


def register(code, mobile):
    """
    注册接口
    :param code:
    :param mobile:
    :return:
    """
    json_data = {"password": "123456", "username": str(mobile), "code": str(code)}
    response = api_util.register_mobile(json=json_data)
    return process_response(response)


def login(username, password):
    """
    登陆接口
    :param username:
    :param password:
    :return:
    """
    json_data = {"username": str(username), "password": str(password)}
    response = api_util.user_login(json=json_data)
    return process_response(response)


def add_shopping_cart(params, token):
    """
    添加购物车
    :param token:
    :param params:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.shopping_add(json=params, headers=headers)
    return process_response(response)


def add_message(data, files, token):
    """
    增加留言
    :param data:
    :param files:
    :param token:
    :return:
    """
    headers = {
        "Authorization": "JWT " + token
    }
    response = api_util.add_message(data=data, files=files, headers=headers)
    return process_response(response)

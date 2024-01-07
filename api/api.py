from core.api_util import Api


def mobile_query(params):
    response = Api().get_mobile_belong(params=params)
    return response.json()

def mobile_json(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    response = Api().post_data(json=json_data)
    return response.json()
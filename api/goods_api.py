from core.api_util import api_util
from utils.response_utils import process_response


def get_banner():
    """
    获取首页banner
    :return:
    """
    response = api_util.banner()
    return process_response(response)

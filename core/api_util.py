from core.rest_client import RestClient


# 用户中心接口地址
class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get("/shouji/query", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)


api_util = Api()
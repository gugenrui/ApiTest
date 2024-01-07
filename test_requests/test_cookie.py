import requests
req = requests.session()  #登录后保存cookie到req
#req = requests
#创建一个会话
url = 'http://sellshop.5istudy.online/sell/user/login'
data = {
    'username':'test01',
    'password':'123456'
}
#登录，req保存了cookie或者session
res = req.post(url,data)
url2 = 'http://sellshop.5istudy.online/sell/seller/order/list?page=2&size=10'
res2 = req.get(url2)
print(res2.text)
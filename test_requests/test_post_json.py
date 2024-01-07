import requests

# json_data = {
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# }
# r = requests.post(url="http://jsonplaceholder.typicode.com/posts", json=json_data)
#
# print(r.status_code)
# print(r.json())

data = {
    "text": "hello"
}

r = requests.post(url="https://dict.youdao.com/keyword/key", data=data)
print(r.status_code)
print(r.json())

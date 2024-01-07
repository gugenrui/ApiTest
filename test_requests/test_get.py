import requests

r = requests.get("https://api.github.com/events")
print(r.status_code) #接口状态返回码
print(r.json())      #接口json
print(r.text)        #接口返回文本
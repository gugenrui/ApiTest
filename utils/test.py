import os

# 当前目录
print(os.path.realpath(__file__))
# 找到当前父级目录utils
print(os.path.dirname(os.path.realpath(__file__)))
# 找到最上级目录ApiTest
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# 找到data.yaml目录
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml"))

# # import random
# #
# #
# # def red_packets(t_money, t_packets):
# #     min_red = 0.01
# #     red_list = []
# #     for i in range(t_packets - 1):
# #         money = round(random.uniform(min_red, t_money * 0.9), 2)
# #         t_money -= money
# #         red_list.append(money)
# #
# #     red_list.append(round(t_money, 2))
# #
# #     return red_list
# #
# #
# # if __name__ == '__main__':
# #     a = red_packets(100, 10)
# #     print(a)
#
# def check_str(string):
#     a = []
#     for char in string:
#         if char == "(" or char == "{" or char == "[":
#             a.append(char)
#         elif (char == ")" and len(a) > 0 and a[-1] == "(") or (char == "}" and len(a) > 0 and a[-1] == "{") or (
#                 char == "]" and len(a) > 0 and a[-1] == "["):
#             a.pop()
#         else:
#             return False
#     if len(a) != 0:
#         return False
#     return True
#
#
# if __name__ == '__main__':
#     print(check_str("({[]})"))

import json


def compare_twojson(json1, json2):
    json1_qudebug = json.dumps(json1, indent=None)
    json2_qudebug = json.dumps(json2, indent=None)
    if isinstance(json1_qudebug, str) and isinstance(json2_qudebug, str):
        dict1 = json.loads(json1_qudebug)
        dict2 = json.loads(json2_qudebug)

    elif isinstance(json1_qudebug, dict) and isinstance(json2_qudebug, dict):
        dict1 = json1_qudebug
        dict2 = json2_qudebug

    else:
        return False
    a = recursive_compare(dict1,dict2)
    return a

def recursive_compare(dict1, dict2):
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            return False

    for key in dict2:
        if key not in dict1:
            return False
    return True

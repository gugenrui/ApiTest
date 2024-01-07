import pytest


# 数组形式
# @pytest.mark.parametrize("name,word", [["李白", "大河之剑天上来"], ["孙尚香", "大小姐驾到"], ["鲁班", "鲁班大师，智商250"], ["安其拉", "火烧屁屁喽"]])
# # def test_parametrize_02(name, word):
# #     # print(f'{name}的台词是"{word}"')
# #     print('%s的台词是"%s"'% (name, word))

# 元组形式
# @pytest.mark.parametrize("name,word", [("李白", "大河之剑天上来"), ("孙尚香", "大小姐驾到"), ("鲁班", "鲁班大师智商250"), ("安其拉", "火烧屁屁喽")])
# def test_parametrize_02(name, word):
#     #print(f'{name}的台词是"{word}"')
#     print('%s的台词是"%s"' % (name, word))

@pytest.mark.parametrize("name,word", [["李白", "大河之剑天上来"]])
def test_parametrize_02(name, word):
    #print(f'{name}的台词是"{word}"')
    print('%s的台词是"%s"' % (name, word))

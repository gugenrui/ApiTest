# 用户中心conftest
from utils.log_util import logger
from utils.mysql_util import db


# 查询验证码
def get_code(mobile):
    sql = "SELECT code FROM users_verifycode WHERE mobile = '%s' ORDER BY id DESC LIMIT 1;" % mobile
    result = db.select_db_one(sql)
    return result['code']


# 删除用户
def delete_user(mobile):
    sql = "DELETE FROM users_userprofile WHERE mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')


# 删除用户注册手机号
def delete_code(mobile):
    sql = "DELETE FROM users_verifycode WHERE mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')


# 查询购物车good的数量
def get_shop_cart_num(username, good_id):
    userid = user_id(username)
    # 查询数量
    sql = "SELECT nums FROM trade_shoppingcart WHERE user_id = %d AND goods_id = %d;" % (userid, good_id)
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['nums']


# 查询user_id
def user_id(mobile):
    sql = "SELECT id FROM users_userprofile WHERE mobile = '%s';" % mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['id']

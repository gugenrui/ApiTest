import pymysql

from utils.log_util import logger
from utils.read import base_data

data = base_data.read_ini_host()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWORD'],
    "db": data['MYSQL_DB']
}


class MysqlDb:
    def __init__(self):
        # mysql连接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    # 查询多条
    def select_db_all(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'sql执行结果：{result}')
        return result

    # 执行增删改
    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()

if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_one(
        "SELECT code FROM users_verifycode WHERE mobile = '15115112563' ORDER BY id DESC LIMIT 1;")
    print(result['code'])

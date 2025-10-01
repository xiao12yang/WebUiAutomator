import pymysql
import pymysql.cursors
from util_tools.handle_data.configParse import ConfigParser
from util_tools.logs_util.recordlog import logs

config = ConfigParser()

class ConnectMysql:
    """
    连接MYSQL数据库，进行增删改查
    """
    def __init__(self):
        self.conf = {
            'host': config.get_mysql_conf('host'),
            'port': config.get_mysql_conf('port'),
            'user': config.get_mysql_conf('user'),
            'password': config.get_mysql_conf('password'),
            'database': config.get_mysql_conf('database'),
        }

        try:
            self.conn = pymysql.connect(**self.conf)
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            logs.info(f'数据库连接成功【数据库ip：{self.conf.get("host")}】')
        except Exception as e:
            logs.error(f'数据库连接异常【原因：{e}】')

    def query(self, sql,fetchall=False):
        """
        查询数据库
        :param sql: SQL语句
        :param fetch: 是否查询全部数据
        :return:
        """
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            if fetchall:
                return self.cursor.fetchall()
            else:
                return self.cursor.fetchone()
        except Exception as e:
            logs.error(f'查询数据库内容出现异常【原因：{e}】')
        finally:
            self.close()




    def close(self):
        """
        断开数据库连接
        :return:
        """
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        return True

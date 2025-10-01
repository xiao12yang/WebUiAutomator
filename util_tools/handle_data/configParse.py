import configparser
from config.setting import FILE_PATH
from util_tools.logs_util.recordlog import logs

class ConfigParser:

    """
    解析.ini后最的配置文件
    """
    def __init__(self,file_path=FILE_PATH['ini']):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.read_config()

    def read_config(self):
        self.config.read(self.file_path)

    def get_value(self,section,option):
        """
        获取配置文件的值
        :param section: 参数头
        :param option: 下级参数key值
        :return:
        """
        try:
            return self.config.get(section,option)
        except Exception as e:
            logs.error(f'解析配置文件异常【文件路径：{self.file_path}，原因：{e}】')

    def get_mysql_conf(self,option):
        """
        获取MySQL数据的配置参数
        :param option:
        :return:
        """
        return self.get_value('MySql',option)

# 处理json文件

import json
from util_tools.logs_util.recordlog import logs
def read_json(file_path):
    """
    读取json数据
    :param file_path: 
    :return: 返回类型为列表类型
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            data_list = [tuple(data_dict.values()) for data_dict in data]
        logs.info(f'json文件读取成功【文件位置：{file_path}】')
        return data_list
    except Exception as e:
        logs.error(f'json文件读取失败【出现未知原因：{e}】')


if __name__ == '__main__':
    print(read_json('../../data/login_success.json'))
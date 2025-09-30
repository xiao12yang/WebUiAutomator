import yaml
from util_tools.logs_util.recordlog import logs

def read_yaml(file_path):
    """
    yaml文件数据格式要么是数组嵌套数组，要么是数组嵌套字典
    :param file_path:
    :return:
    """
    data_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            result = yaml.safe_load(f)
            if isinstance(result[0],list):
                data_list = result
            else:
                data_list = [tuple(data_dict.values()) for data_dict in result]
        logs.info(f'yaml文件读取成功【yaml文件位置：{file_path}】')
        return data_list
    except Exception as e:
        logs.error(f'yaml文件读取异常【异常原因：{e}】')


if __name__ == '__main__':
    data = read_yaml('../../data/login.yaml')
    print(data)
    print(len(data))
    print(type(data))

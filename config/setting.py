import os
import sys

DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH) #分析当前的根目录，存储到系统路径中，以确保在不同环境下都能找到根目录下的文件

#显示等待时间设置，默认为10s
WAIT_TIME = 10

# 文件路径
FILE_PATH = {
    'log': os.path.join(DIR_PATH, 'log'),
    'screenshot': os.path.join(DIR_PATH, 'screenshot'),
}


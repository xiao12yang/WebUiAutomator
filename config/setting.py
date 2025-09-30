import os
import sys

DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(DIR_PATH) #分析当前的根目录，存储到系统路径中，以确保在不同环境下都能找到根目录下的文件

#显示等待时间设置，默认为10s
WAIT_TIME = 10

# 设置浏览器
browser_type = 'edge'

# 文件路径
FILE_PATH = {
    'log': os.path.join(DIR_PATH, 'log'),
    'screenshot': os.path.join(DIR_PATH, 'screenshot'),
}


# 钉钉机器人
# 是否发送消息
is_dd_msg = True
secret = 'SECccaf2ff601c590f5745c83bd88014610cb7f99a696b13e923de38468284d5da2'
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=b1b0a9d43da44c2812cd8dcd0bd1f55b8e4017bfd952eadffe0095482d032aef'

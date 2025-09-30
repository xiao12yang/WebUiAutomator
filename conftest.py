import time
from datetime import timedelta
from util_tools.other_util.dingding_rebot import send_dd_msg
from config.setting import is_dd_msg
import pytest

@pytest.fixture(scope="session", autouse=True)
def testStart():
    print("testStart")


def pytest_sessionstart(session):
    """
    再测试会话开始时记录时间
    :param session:
    :return:
    """
    session.config.session_start_time = time.time()

def pytest_terminal_summary(terminalreporter,exitstatus,config):
    """
    Pytest框架中预定义的钩子函数，用于再测试结束后自动收集测试结果
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """
    testcase_total = terminalreporter._numcollected
    pass_num = len(terminalreporter.stats.get('passed',[]))
    fail_num = len(terminalreporter.stats.get('failed',[]))
    error_num = len(terminalreporter.stats.get('error',[]))
    skip_num = len(terminalreporter.stats.get('skipped',[]))
    duration = 0
    session_start_time = getattr(config,'session_start_time',None)
    if session_start_time:
        duration = round(time.time() - session_start_time,2)
    formatter_duration = str(timedelta(seconds=duration)).split('.')[0]

    # 统计通过率、失败率、错误率
    pass_rate = f'{(pass_num/testcase_total)*100:.2f}%' if testcase_total > 0 else 'N/A'
    error_rate = f'{(error_num/testcase_total)*100:.2f}%' if testcase_total > 0 else 'N/A'
    fail_rate = f'{(fail_num/testcase_total)*100:.2f}%' if testcase_total > 0 else 'N/A'

    summary = f"""
    UI自动化测试结果，通知如下，具体执行结果：
    测试用例总数量：{testcase_total}
    测试用例用过数量：{pass_num}
    通过率：{pass_rate}
    测试用例失败数量：{fail_num}
    失败率：{fail_rate}
    测试用例错误数量：{error_num}
    错误率：{error_rate}
    测试用例跳过数量：{skip_num}
    执行总时长：{formatter_duration}
    """
    if is_dd_msg:
        send_dd_msg(summary)

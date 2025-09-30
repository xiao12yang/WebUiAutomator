import pytest
from selenium import webdriver
from util_tools.logs_util.recordlog import logs
from config.setting import browser_type

def pytest_sessionstart(session):
    logs.info('********开始测试*********')

def pytest_sessionfinish(session, exitstatus):
    logs.info('********结束测试*********')

@pytest.fixture(scope='function',autouse=True)
def log_output():
    logs.info('********测试用例开始执行*********')
    yield
    logs.info('********测试用例结束执行*********')

@pytest.fixture()
def get_driver():
    # 初始化浏览器对象
    driver = None
    browser_map = {
        'Chrome': webdriver.Chrome,
        'Firefox': webdriver.Firefox,
        'Edge': webdriver.Edge
    }
    if browser_type.capitalize() in browser_map:
        driver = browser_map.get(browser_type.capitalize())()
        logs.info(f'打开浏览器成功【浏览器名称：{browser_type.capitalize()}】')
    # 设置一个全局的隐式等待时间
    driver.implicitly_wait(10)
    # 最大化窗口
    driver.maximize_window()
    yield driver
    driver.quit()
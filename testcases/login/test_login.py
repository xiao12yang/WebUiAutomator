from time import sleep

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pageObject.login_page.login_page import LoginPage
from util_tools.handle_data.operateJson import read_json
from util_tools.handle_data.operateYaml import read_yaml
from util_tools.handle_data.operateExcel import ExcelDataReader
from util_tools.logs_util.recordlog import logs


class TestLogin:
    @pytest.mark.parametrize('username,password',read_json('./data/login_success.json'))
    def test_login_success(self,username,password,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login(username,password)
        login_page.is_element_present((By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font[@class="f4_b"]'))

    # @pytest.mark.parametrize('username,password',read_yaml('./data/login.yaml'))
    @pytest.mark.parametrize('username,password',ExcelDataReader('./data/login_failed.xlsx').read_all_row(sheet_name='Sheet1'))
    def test_login_fail_01(self,username,password,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login(username, password)
        login_page.assert_title('系统提示')

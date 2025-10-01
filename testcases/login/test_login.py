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
    @pytest.mark.parametrize('username,password',read_json('./data/login.json'))
    def test_login_success(self,username,password,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login(username,password)
        result = WebDriverWait(get_driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font[@class="f4_b"]'))
        )
        result = result.text
        assert username in result,'测试失败'

    # @pytest.mark.parametrize('username,password',read_yaml('./data/login.yaml'))
    @pytest.mark.parametrize('username,password',ExcelDataReader('./data/login_testdata.xlsx').read_all_row(sheet_name='Sheet1'))
    def test_login_fail(self,username,password,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login(username, password)

        result = WebDriverWait(get_driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.boxCenterList div p:first-child'))
        )
        result = result.text
        assert "用户名或密码错误" in result,'测试失败'
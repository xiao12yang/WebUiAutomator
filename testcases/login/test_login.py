from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pageObject.login_page.login_page import LoginPage
from util_tools.logs_util.recordlog import logs


class TestLogin:
    def test_login_success(self,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login('admin111','admin111')

        result = WebDriverWait(get_driver, 10).until(
            ec.presence_of_element_located((By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font[@class="f4_b"]'))
        )
        result = result.text
        assert "admin111" in result,'测试失败'

    def test_login_fail(self,get_driver):
        login_page = LoginPage(get_driver)
        login_page.login('admin111', 'admin1111')

        result = WebDriverWait(get_driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.boxCenterList div p:first-child'))
        )
        result = result.text
        assert "用户名或密码错误" in result,'测试失败'
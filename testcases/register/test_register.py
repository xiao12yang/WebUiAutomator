import pytest
from selenium.webdriver.common.by import By
from pageObject.register_page.register_page import RegisterPage
from util_tools.handle_data.operateExcel import ExcelDataReader


class TestRegister:

    @pytest.mark.parametrize('data',ExcelDataReader('./data/register_data.xlsx').read_all_row(sheet_name='success'))
    def test_register_success(self, data, get_driver):
        register_page = RegisterPage(get_driver)
        register_page.click_register(*data)
        register_page.is_element_present((By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font[@class="f4_b"]'))
    def test_register_fail(self):
        pass

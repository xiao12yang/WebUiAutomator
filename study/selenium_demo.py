from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost/ecshop/admin/index.php")
driver.maximize_window()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('123')

driver.switch_to.new_window()
driver.get("https://www.baidu.com")



input('输入回车结束')

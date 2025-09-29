
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://leafground.com/frame.xhtml')
frame = wd.find_element(By.XPATH,'//iframe[@src="default.xhtml"]')
# 切换到子窗口
wd.switch_to.frame(frame)
wd.find_element(By.ID,'Click').click()
# 切换到父窗口
wd.switch_to.default_content()
input('输入回车结束...')
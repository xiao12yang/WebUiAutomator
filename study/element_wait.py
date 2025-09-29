from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Chrome()
wd.maximize_window()
wd.get("https://leafground.com/alert.xhtml")
# sleep(3) # 强制等待
# 显示等待
WebDriverWait(wd,1).until(
    EC.presence_of_element_located((By.ID,'j_idt88:j_idt91'))
)

# 隐式等待
wd.implicitly_wait(10)
input('input Enter to over...')
wd.quit()
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get('https://leafground.com/alert.xhtml')
# alert = WebDriverWait(wd,10).until(
#     EC.presence_of_element_located((By.ID,'j_idt88:j_idt91'))
# )
# alert = WebDriverWait(wd,10).until(
#     EC.presence_of_element_located((By.ID,'j_idt88:j_idt93'))
# )
alert = WebDriverWait(wd,10).until(
    EC.presence_of_element_located((By.ID,'j_idt88:j_idt95'))
)
alert.click()
sleep(1)
#
# wd.switch_to.alert.accept() # 确定
# wd.switch_to.alert.dismiss() # 取消

input('enter...')
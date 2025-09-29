from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get("http://localhost/ecshop/user.php?act=register")
wd.maximize_window()
# wd.find_element(By.ID,'username').send_keys('admin')
# wd.find_element(By.NAME,'email').send_keys('weimishi537@163.com')
# wd.find_elements(By.CLASS_NAME,'inputBg')[2].send_keys('123456')
# wd.find_element(By.CSS_SELECTOR,'.box input') #
# wd.find_element(By.CSS_SELECTOR,'[type="text"]') # 属性选择器
# wd.find_element(By.CSS_SELECTOR,'table>tr:nth-child(2)>tr:nth-child(2)')
sleep(2)
# wd.find_element(By.LINK_TEXT,"我已有账号，我要登录").click()
# wd.find_element(By.PARTIAL_LINK_TEXT,'我已有账号').click()
# wd.find_element(By.XPATH,'/html/body//input[@name="username"]').send_keys('123')

# wd.find_element(By.XPATH,'//input[@name="username"]').send_keys('XPATH')
# wd.find_element(By.XPATH,'//a[text()="用户协议"]').click()
# wd.find_element(By.XPATH,'//*[contains(text(),"忘记密码")]').click()
# wd.find_element(By.XPATH,'//*[@id="username"]').send_keys("元素属性选择")
wd.find_element(By.XPATH,'//*[@id="username" and @name="username"]').send_keys("逻辑运算符结合选择器")

input('输入回车结束')
wd.quit()
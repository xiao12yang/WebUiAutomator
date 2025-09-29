from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
wd = webdriver.Chrome()
wd.get("http://localhost/ecshop/user.php?act=register")
wd.maximize_window()
sleep(2)
# wd.find_element(By.XPATH,'//input[@id="username"]').send_keys("用户名")
# sleep(2)
# 下拉框处理
# ele = wd.find_element(By.XPATH,'//select[@name="sel_question"]')
# select = Select(ele)
# select.select_by_index(2)
# select.deselect_all()

# wd.find_element(By.XPATH,'//a[text()="您忘记密码了吗？" and @href="user.php?act=get_password"]').click()
# wd.find_element(By.XPATH,'//input[@name="Submit" and @class="us_Submit_reg"]').click()
# alert = wd.switch_to.alert
# sleep(2)
# alert.accept()
# alert.dismiss()

# 滑动条处理
wd.get('https://leafground.com/input.xhtml')
sleep(2)
# wrap = wd.find_element(By.ID,'j_idt106:j_idt120')

# print(wrap)
# wrap_width = wrap.size['width']
# # 计算要拖动的偏移量
# offset = wrap_width/5
# action = ActionChains(wd)
# action.click(wrap).move_by_offset(offset,0).release().perform()
# 其中release()是释放鼠标，


# 使用文本框上的向上箭头模拟自增
# number_input = wd.find_element(By.ID,'j_idt106:j_idt118_input')
# number_input.clear()
# number_input.send_keys(Keys.ARROW_UP)

# 日期选择
# ele = wd.find_element(By.ID,'j_idt106:j_idt116_input')
# ele.click()
# # 定位到日期选择元素
# date_ele = wd.find_element(By.XPATH,'//*[@id="j_idt106:j_idt116_panel"]/div/div[2]/table/tbody/tr[3]/td[5]/a')
# date_ele.click()

# 截图
# wd.save_screenshot('src.png')

# 模拟鼠标键盘操作
# 1、键盘按键
ActionChains(wd).send_keys(Keys.CONTROL + "C").perform()



input('input ENTER to over...')

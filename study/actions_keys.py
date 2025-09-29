from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wd = webdriver.Chrome()
wd.get('https://leafground.com/input.xhtml')
WebDriverWait(wd, 10).until(
    EC.presence_of_element_located(("tag name", "body"))
)
wd.maximize_window()
# 定位到多行文本框
lines_ele = wd.find_element(By.ID,'j_idt88:j_idt101')
lines_ele.send_keys('456486978')
sleep(1)
# 模拟键盘回车定位
ActionChains(wd).send_keys(Keys.ENTER).perform()
lines_ele.send_keys('第二行文字')
sleep(1)
target = wd.find_element(By.ID,'j_idt88:j_idt103_editor')
ActionChains(wd).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()



# ActionChains(wd).context_click(lines_ele).perform()
#
# ele = wd.find_element(By.ID,'menuform:j_idt39')
# ActionChains(wd).move_to_element(ele).perform()
# img_start = wd.find_element(By.ID,'form:j_idt89:0:j_idt98')
# img_end = wd.find_element(By.XPATH,'//span[contains(@class,"customer-badge") and text()="QUALIFIED"]')
# 拖拽
# ActionChains(wd).drag_and_drop(lines_ele, target).perform()

# ActionChains(wd).move_by_offset(0,600).perform()
# 使用js执行向下滚动到页面底部
wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")



input('input ENTER to over...')
wd.quit()


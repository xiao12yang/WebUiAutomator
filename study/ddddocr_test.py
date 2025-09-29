# 安装的 pillow 版本 要 9.5, 不能是 10， 否则 会有错误 module 'PIL.Image' has no attribute 'ANTIALIAS'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddddocr

ocr = ddddocr.DdddOcr()

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging']) # for ignore warning and error
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get('http://localhost/ecshop/admin/privilege.php?act=login')

time.sleep(2) # 这里出现captcha时间有点长，等待2秒

while True:
    # 获取元素展示内容为图片数据
    pngData = driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/img').screenshot_as_png

    # with open('d:/tmp1.png', 'wb') as f:
    #     f.write(pngData)

    res = ocr.classification(pngData)
    print('验证码是', res)

    ch = input('')
    if ch != '':
        break

    driver.refresh()
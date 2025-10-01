import os.path
from time import sleep

import ddddocr
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from config.setting import WAIT_TIME,FILE_PATH
from selenium.webdriver.support import expected_conditions as ec
from util_tools.logs_util.recordlog import logs
from selenium.common import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from datetime import datetime




class BasePage(object):
    """
    封装浏览器的一些操作，对象webdriver里面的一些方法进行二次开发
    此类封装所有的操作，所有页面继承该类
    """

    def __init__(self, driver):
        """
        显示等待浏览器对象初始化
        :param driver:
        """
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, WAIT_TIME)

    def window_max(self):
        """
        浏览器窗口最大化
        :return:
        """
        self.__driver.maximize_window()

    def window_full(self):
        """
        浏览器全屏窗口
        :return:
        """
        self.__driver.fullscreen_window()

    def screenshot(self,image_name):
        """
        封装浏览器截屏
        :return:
        """
        try:
            current_time = datetime.now().strftime('%Y%m%d%H%M%S') # 获取当前时间
            file_name = f'{image_name}-{current_time}.png'
            file_path = os.path.join(FILE_PATH['screenshot'],file_name)
            self.__driver.get_screenshot_as_file(file_path)
            logs.info(f'浏览器截屏成功【截屏存储路径：{file_path}】')
        except Exception as e:
            logs.error(f'浏览器截屏异常【原因：{e}】')

    def open_url(self,url):
        """
        打开测试页面
        :return:
        """
        self.__driver.get(url)

    @property
    def current_url(self):
        """
        获取当前页面url
        :return:
        """
        return self.__driver.current_url
    @property
    def title(self):
        """
        获取页面标题
        :return:
        """
        return self.__driver.title


    def refresh(self):
        """
        页面刷新
        :return:
        """
        self.__driver.refresh()

    @property
    def switch_to(self):
        """
        切换switch_to
        :return:
        """
        return self.__driver.switch_to

    def iframe(self,frame):
        """
        切换到iframe框架中
        :return:
        """
        self.switch_to.frame(frame)

    def exit_iframe(self):
        """
        退出iframe框架
        :return:
        """
        self.switch_to.default_content()

    @property
    def alert(self):
        """
        切换到alert弹框处理
        :return:
        """
        # return self.switch_to.alert
        return self.__wait.until(
            ec.alert_is_present() # 等待直到页面出现弹框，存在就返回alert，不存在就返回False
        )

    def alert_confirm(self):
        """
        点击alert确认
        :return:
        """
        self.alert.accept()

    def alert_cancel(self):
        """
        alert取消操作
        :return:
        """
        self.alert.dismiss()


    def location_element(self,by,value):
        """
        find_element的二次封装
        :param by: 定位方式，如By.ID,By.XPATH
        :param value: 定位表达式
        :return:
        """
        try:
            element = self.__wait.until(
                ec.presence_of_element_located((by,value))
            )
            logs.info(f'元素查找成功【定位方式：{by} - 表达式：{by}={value}】')
            return element
        except TimeoutException as e:
            logs.error(f'元素查找失败【定位方式：{by} - 表达式：{by}={value} - 超时时间：{WAIT_TIME}s】')
            # raise
        except Exception as e:
            logs.error(f'元素查找失败【出现未知异常：{e}】')
            # raise

    def location_elements(self,by,value):
        """
        find_elements的二次封装，定位元素列表
        :param by: 定位方式，如By.ID,By.XPATH
        :param value: 定位表达式
        :return:
        """
        try:
            element = self.__wait.until(
                ec.presence_of_all_elements_located((by,value))
            )
            logs.info(f'元素列表查找成功【定位方式：{by} - 表达式：{by}={value}】')
            return element
        except TimeoutException as e:
            logs.error(f'元素列表查找失败【定位方式：{by} - 表达式：{by}={value} - 超时时间：{WAIT_TIME}s】')
            raise
        except Exception as e:
            logs.error(f'元素列表查找失败【出现未知异常：{e}】')
            raise



    def click(self,locator:tuple,force=False):
        """
        封装点击操作
        :param locator: 元组类型（tuple），定位元素信息，如(By.ID,"123564")
        :param force: 可选，表示是否使用强制点击，默认为False
        :return:
        """
        try:
            element = self.location_element(*locator)
            if not force:
                element.click()
                logs.info(f'元素点击成功【目标：{locator} - 点击成功】')
            else:
                self.__driver.execute_script("arguments[0].click();", element)
                logs.info(f'元素强制点击成功【目标：{locator} - 点击成功】')
        except ElementClickInterceptedException as e:
            logs.error(f'元素点击失败【元素被遮挡：{locator}】')
            raise
        except ElementNotInteractableException as e:
            logs.error(f'元素点击失败【元素不可交互：{locator}】')
            raise
        except StaleElementReferenceException as e:
            logs.error(f'元素点击失败【元素已过期：{locator}】')
            raise
        except Exception as e:
            logs.error(f'元素点击失败【未知异常：{e}】')
            raise


    def send_keys(self,locator:tuple,data):
        """
        对send_keys进行二次封装
        :param locator: 元组类型（tuple），定位元素信息，如(By.ID,"123564")
        :param data: 输入的内容
        :return:
        """
        try:
            element = self.location_element(*locator)
            element.send_keys(data)
            logs.info(f'文本输入成功【目标：{locator} - 文本输入：{data}】')
        except ElementNotInteractableException as e:
            # 元素不可交互（最常见）
            logs.error(f'文本输入失败【元素不可交互：{locator}】')
            raise
        except ElementNotVisibleException as e:
            # 元素不可见
            logs.error(f'文本输入失败【元素不可见：{locator}】')
            raise
        except StaleElementReferenceException as e:
            # 元素已过期
            logs.error(f'文本输入失败【元素已过期：{locator}】')
            raise
        except InvalidElementStateException as e:
            # 元素状态无效（如只读输入框）
            logs.error(f'文本输入失败【元素状态无效：{locator}】')
            raise
        except Exception as e:
            logs.error(f'文本输入失败【出现未知原因：{e}】')

    def enter(self):
        """
        封装键盘回车
        :return:
        """
        try:
            ActionChains(self.__driver).send_keys(Keys.ENTER).perform()
            logs.info(f'键盘回车键执行成功')
        except Exception as e:
            logs.error(f'键盘回车键执行失败【出现未知原因：{e}】')
            raise

    def right_click(self,locator:tuple):
        """
        右键点击
        :return:
        """
        try:
            ele = self.location_element(*locator)
            ActionChains(self.__driver).context_click(ele).perform()
            logs.info(f'右键点击执行成功【目标：{locator}】')
        except Exception as e:
            logs.error(f'右键点击执行失败【出现未知原因：{e}】')
            raise

    def double_click(self,locator:tuple):
        """
        双击操作
        :param locator:
        :return:
        """
        try:
            ele = self.location_element(*locator)
            ActionChains(self.__driver).double_click(ele).perform()
            logs.info(f'鼠标双击执行成功【目标：{locator}】')
        except Exception as e:
            logs.error(f'鼠标双击执行失败【出现未知原因：{e}】')
            raise

    def clear(self,locator:tuple):
        """
        清空
        :param locator:
        :return:
        """
        try:
            element = self.location_element(*locator)
            element.clear()
            logs.info(f'清空文本执行成功【目标：{locator}】')
        except Exception as e:
            logs.error(f'清空文本执行失败【出现未知原因：{e}】')
            raise e

    # 使用tesseract
    def ocr_captcha_tesseract(self,locator:tuple):
        """
        1）定位到图形验证码，保存图片
        2）调用Image去打开图像
        3）调用pytesseract模块进行OCR识别
        :param locator: 定位方式和表达式（元组）
        :return:
        """
        captcha_element = self.location_element(*locator)
        # 截取图形验证码
        captcha_path = FILE_PATH['screenshot'] + '/captcha.png'
        captcha_element.screenshot(captcha_path)
        # 调用Image模块打开图像
        captcha_image = Image.open(captcha_path)
        try:
            # 调用pytesseract进行OCR识别
            captcha_text = pytesseract.image_to_string(captcha_image)
            logs.info(f'识别验证码成功【目标{locator}，验证码：{captcha_text}】')
            return captcha_text
        except pytesseract.pytesseract.TesseractNotFoundError as e:
            logs.error(f'找不到tesseract模块，这是因为pytesseract模块依赖于TesseractOCR引擎来进行图像识别!')
        except Exception as e:
            logs.error(f'识别验证码失败【出现未知原因：{e}】')

    def ocr_captcha_ddddOcr(self,locator:tuple):
        """
        使用ddddocr获取验证码
        :param locator:
        :return:
        """
        try:
            ocr = ddddocr.DdddOcr()
            pngData = self.location_element(*locator).screenshot_as_png
            captcha = ocr.classification(pngData)
            return captcha
        except Exception as e:
            logs.error(f'识别验证码失败【出现未知原因：{e}】')

    def selects_by_index(self,locator:tuple,index):
        """
        封装通过索引选择下拉菜单选项
        :param locator:
        :param data:
        :return:
        """
        try:
            element = self.location_element(*locator)
            select = Select(element)
            select.select_by_index(index)
            logs.info(f'Select选项选择成功【索引值：{index}，选项内容：{select.options[index].text}】')
        except NoSuchElementException as e:
            logs.error(f'Select选项选择失败【原因：索引：{index}，超出有效索引】')
        except Exception as e:
            logs.error(f'Select选项选择异常【原因：{e}】')




    # 断言元素是否存在
    def is_element_present(self,locator:tuple):
        """
        判断函数是否存在
        :param locator:
        :return:
        """
        try:
            element = self.location_element(*locator)
            assert element,f'存在断言失败【原因：{locator}元素不存在】'
            logs.info(f'断言成功【元素-{locator}-存在于页面中】')
        except AssertionError as a:
            logs.error(a)
            raise a
        except Exception as e:
            logs.error(f'断言出现异常【原因：{e}】')
            raise

    # 断言标题是否存在于页面的标题中
    # 需要考虑元素查找的执行速度，当查找速度太快，页面还没跳转就被获取当前标题
    def assert_title(self,expect_title):
        """
        断言预期标题文本是否包含在实际页面的标题中
        :param expect_title:
        :return:
        """
        try:
            assert expect_title in self.title,f'包含断言失败【预期结果："{expect_title}"不包含在实际结果：{self.title}】'
            logs.info(f'包含断言成功【预期结果："{expect_title}"包含在实际结果：{self.title}】')
        except AssertionError as e:
            logs.error(e)
            raise
        except Exception as e:
            logs.error(f'断言出现异常【原因：{e}】')
            raise
    # 包含断言
    # 相等断言
    # 不相等断言
    # 数据库断言
    # ...











if __name__ == '__main__':
    wd = webdriver.Chrome()
    bros = BasePage(wd)
    bros.open_url('http://localhost/ecshop/admin/privilege.php?act=login')
    print(bros.current_url)
    bros.send_keys((By.XPATH,'//input[@name="username"]'),'admin')
    bros.send_keys((By.XPATH,'//input[@name="password"]'),'admin123456')

    captcha = bros.ocr_captcha_ddddOcr((By.XPATH,'/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/img'))
    bros.send_keys((By.XPATH,'//input[@name="captcha"]'),captcha)
    sleep(2)
    bros.screenshot('登录页面')


    input('输入回车结束...')

# 后面记得回来完善日志记录
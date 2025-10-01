from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from util_tools.basePage import BasePage

# 登录页面类
class LoginPage(BasePage):

    url = 'http://localhost/ecshop/user.php'
    # 用户名
    username = (By.NAME, 'username')
    # 密码
    password = (By.NAME, 'password')
    # 登录按钮
    submit = (By.NAME, 'submit')
    # # 断言结果
    # assert_ele = (By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font[@class="f4_b"]')

    # 登录操作
    def login(self,user_naem,pass_word):
        self.open_url(self.url)
        # 浏览器窗口最大化
        self.window_max()
        # 输入用户名
        self.send_keys(self.username,user_naem)
        # 输入密码
        self.send_keys(self.password,pass_word)
        # 点击登录
        self.click(self.submit)






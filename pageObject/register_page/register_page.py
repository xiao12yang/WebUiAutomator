from selenium.webdriver.common.by import By
from util_tools.basePage import BasePage


# 注册页面类
class RegisterPage(BasePage):
    url = "http://localhost/ecshop/user.php?act=register"
    # 用户名
    username = (By.ID, 'username')
    # email
    email = (By.ID, 'email')
    # 密码
    password = (By.ID, 'password1')
    # 确认密码
    confirm_password = (By.ID, 'conform_password')
    # MSN
    MSN = (By.NAME, 'extend_field1')
    # QQ
    qq = (By.NAME, 'extend_field2')
    # 办公电话
    office_number = (By.NAME, 'extend_field3')
    # 家庭电话
    family_number = (By.NAME, 'extend_field4')
    # 手机
    phone = (By.NAME, 'extend_field5')
    # 密码提示问题
    selects_of_password_hint_question = (By.NAME, 'sel_question')
    # 密码问题答案
    password_security_question_answer = (By.NAME, 'passwd_answer')
    # 勾选：我已看过并接收《用户协议》
    user_agreement = (By.NAME, 'agreement')
    # 立即注册按钮
    register_btn = (By.NAME, 'Submit')
    # 我已有账号，我要登录
    return_login_page = (By.XPATH, '/html/body/div[7]/div/form/table/tbody/tr[16]/td[2]/a[1]')
    # 忘记密码
    forget_password = (By.XPATH, '/html/body/div[7]/div/form/table/tbody/tr[16]/td[2]/a[2]')

    def click_register(self, username, email, password, confirm_password, MSN, qq, office_number, family_number, phone,
                       question_index, password_security_question_answer):
        self.open_url(self.url)
        self.send_keys(self.username, username)
        self.send_keys(self.email, email)
        self.send_keys(self.password, password)
        self.send_keys(self.confirm_password, confirm_password)
        self.send_keys(self.MSN, MSN)
        self.send_keys(self.qq, qq)
        self.send_keys(self.office_number, office_number)
        self.send_keys(self.family_number, family_number)
        self.send_keys(self.phone, phone)
        self.selects_by_index(self.selects_of_password_hint_question, int(question_index))
        self.send_keys(self.password_security_question_answer, password_security_question_answer)
        self.screenshot('注册信息')
        self.click(self.register_btn)

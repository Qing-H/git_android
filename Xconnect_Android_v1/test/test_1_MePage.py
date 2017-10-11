import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
#from utils.verify_items import *
from utils.config import Config
from pages.MePage import Me
from appium.webdriver.common.touch_action import TouchAction
from BasePage import Base

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class A_MePageTests(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        path = Config().get('path')
        url = Config().get('url')
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(path)
        desired_caps['noReset'] = True
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        cls.driver = webdriver.Remote(url, desired_caps)
#登录
    def test_login(self):
        phone_num_a = Config().get('phone_num_a')
        password_a = Config().get('password_a')
        me_page = Me(self.driver)
        #me_page.click_me()
        me_page.click_send_et_user_name(phone_num_a)
        me_page.click_send_et_user_password(password_a)
        me_page.click_btn_login()
#登出，取消登出
    # def test_logoff_cancel(self):
    #     me_page = Me(self.driver)
    #     me_page.click_me()
    #     me_page.click_tv_exit()
    #     me_page.click_lef_btn()
#登出，确定登出
    # def test_logoff_confirm(self):
    #     me_page = Me(self.driver)
    #     me_page.click_me()
    #     me_page.click_tv_exit()
    #     me_page.click_right_btn()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ == '__main__':
#     report = "D:\study\Test_Framework\\report" + '\\report.html'
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='Xconnect Test Report', description='MePage测试报告')
#         suite = unittest.TestLoader().loadTestsFromTestCase(A_MePageTests)
#         runner.run(suite)


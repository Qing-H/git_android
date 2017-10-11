import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
import BasePage
#driver = webdriver.Remote(BasePage.Base.url, BasePage.Base.desired_caps)

class Me(BasePage.Base):
    me = 'ctrip.android.xconnect:id/me'
    et_user_name = "ctrip.android.xconnect:id/et_user_name"
    et_user_password = "ctrip.android.xconnect:id/et_user_password"
    btn_login = 'ctrip.android.xconnect:id/btn_login'
    tv_exit = 'ctrip.android.xconnect:id/tv_exit'
    lef_btn = 'ctrip.android.xconnect:id/lef_btn'
    right_btn = 'ctrip.android.xconnect:id/right_btn'



    def click_me(self):
        self.click_wait_button(self.me)

    def click_send_et_user_name(self,phone_num_a):
        self.send(self.et_user_name,phone_num_a)

    def click_send_et_user_password(self,password_a):
        self.send(self.et_user_password,password_a)

    def click_btn_login(self):
        self.click_wait_button(self.btn_login)

    def click_tv_exit(self):
        self.click_wait_button(self.tv_exit)

    def click_lef_btn(self):
        self.click_wait_button(self.lef_btn)

    def click_right_btn(self):
        self.click_wait_button(self.right_btn)


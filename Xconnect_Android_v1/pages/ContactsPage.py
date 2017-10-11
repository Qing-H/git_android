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

class Contacts(BasePage.Base):
    contacts = "ctrip.android.xconnect:id/contacts"
    group_name_1 = Config().get('group_name_1')
    friends_name_1 = Config().get('friends_name_1')
    friends_name_2 = Config().get('friends_name_2')
    friends_name_3 = Config().get('friends_name_3')
    friends_name_4 = Config().get('friends_name_4')
    btn_start_call = "ctrip.android.xconnect:id/btn_start_call"
    iv_hangup_calling = "ctrip.android.xconnect:id/iv_hangup_calling"    #主叫挂断（未接听）
    iv_hangup_called = "ctrip.android.xconnect:id/iv_hangup_called"      #被叫挂断（未接听）
    waiting = "等待对方接听..."
    inviting = "邀请你语音聊天"
    iv_answer_called = "ctrip.android.xconnect:id/iv_answer_called"
    iv_mute = "ctrip.android.xconnect:id/iv_mute"
    iv_speaker = "ctrip.android.xconnect:id/iv_speaker"
    iv_hangup = "ctrip.android.xconnect:id/iv_hangup"    #通话挂断

    def click_contacts(self):
        self.click_wait_button(self.contacts)

    def click_group_name_1(self):
        self.click_wait_button_byname(self.group_name_1)

    def click_friends_name_1(self):
        self.click_wait_button_byname(self.friends_name_1)

    def click_friends_name_2(self):
        self.click_wait_button_byname(self.friends_name_2)

    def click_friends_name_3(self):
        self.click_wait_button_byname(self.friends_name_3)

    def click_friends_name_4(self):
        self.click_wait_button_byname(self.friends_name_4)

    def click_btn_start_call(self):
        self.click_wait_button(self.btn_start_call)

    def click_iv_hangup_calling(self):
        self.click_wait_button(self.iv_hangup_calling)

    def click_iv_hangup_called(self):
        self.click_wait_button(self.iv_hangup_called)

    def click_iv_answer_called(self):
        self.click_wait_button(self.iv_answer_called)

    def click_iv_hangup(self):
        self.click_wait_button(self.iv_hangup)




















































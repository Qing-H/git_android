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

class Conversion(BasePage.Base):
    conversation = "ctrip.android.xconnect:id/conversation"
    rl_item_view = "ctrip.android.xconnect:id/rl_item_view"
    chat_input = "ctrip.android.xconnect:id/chat_input"
    back_ImageButton = "android.widget.ImageButton"
    btn_send_message = "ctrip.android.xconnect:id/btn_send_message"
    chat_btn_more =  "ctrip.android.xconnect:id/chat_btn_more"
    button_img = "ctrip.android.xconnect:id/button_img"
    v_selected = "ctrip.android.xconnect:id/v_selected"
    done = "ctrip.android.xconnect:id/done"
    action_plus = "ctrip.android.xconnect:id/action_plus"
    container = "ctrip.android.xconnect:id/container"
    tv_start_chat = "ctrip.android.xconnect:id/tv_start_chat"
    action_settings = "ctrip.android.xconnect:id/action_settings"
    riv_avatar = "ctrip.android.xconnect:id/riv_avatar"
    quit_discussion = "ctrip.android.xconnect:id/quit_discussion"
    lef_btn = "ctrip.android.xconnect:id/lef_btn"
    right_btn = "ctrip.android.xconnect:id/right_btn"
    tv_discussion_name = "ctrip.android.xconnect:id/tv_discussion_name"
    iv_clean_text = "ctrip.android.xconnect:id/iv_clean_text"
    save = "ctrip.android.xconnect:id/save"
    et_name = "ctrip.android.xconnect:id/et_name"
    old_group_1 = Config().get('old_group_1')
    old_group_2 = Config().get('old_group_2')
    new_group_1 = Config().get('new_group_1')
    new_group_2 = Config().get('new_group_2')
    button_name_1 = Config().get('button_name_1')
    button_name_2 = Config().get('button_name_2')
    button_name_3 = Config().get('button_name_3')

    def click_conversation(self):
        self.click_wait_button(self.conversation)

    def click_rl_item_view_i(self,i):
        self.click_wait_button_i(self.rl_item_view,i)

    def click_old_group_1(self):
        self.click_wait_button_byname(self.old_group_1)

    def click_old_group_2(self):
        self.click_wait_button_byname(self.old_group_2)

    def click_new_group_1(self):
        self.click_wait_button_byname(self.new_group_1)

    def click_new_group_2(self):
        self.click_wait_button_byname(self.new_group_2)

    def click_button_name_1(self):
        self.click_wait_button_byname(self.button_name_1)

    def click_button_name_2(self):
        self.click_wait_button_byname(self.button_name_2)

    def click_button_name_3(self):
        self.click_wait_button_byname(self.button_name_3)

    def click_send(self,msg_1):
        self.send(self.chat_input,msg_1)

    def click_send_et_name(self,name):
        self.send(self.et_name,name)

    def click_back_ImageButton(self):
        self.click_wait_button_byclassname(self.back_ImageButton)

    def click_btn_send_message(self):
        self.click_wait_button(self.btn_send_message)

    def click_chat_btn_more(self):
        self.click_wait_button(self.chat_btn_more)

    def click_button_img(self):
        self.click_wait_button(self.button_img)

    def click_pics(self):#??????
        self.pics(self.v_selected)

    def click_done(self):
        self.click_wait_button(self.done)

    def click_action_plus(self):
        self.click_wait_button(self.action_plus)

    def click_container_i(self,i):
        self.click_wait_button_i(self.container,i)

    def click_search(self,name):
        self.click_wait_button_byname(name)

    def click_tv_start_chat(self):
        self.click_wait_button(self.tv_start_chat)

    def click_action_settings(self):
        self.click_wait_button(self.action_settings)

    def click_riv_avatar_i(self,i):
        self.click_wait_button_i(self.riv_avatar, i)

    def click_quit_discussion(self):
        self.click_wait_button(self.quit_discussion)

    def click_lef_btn(self):
        self.click_wait_button(self.lef_btn)

    def click_right_btn(self):
        self.click_wait_button(self.right_btn)

    def click_tv_discussion_name(self):
        self.click_wait_button(self.tv_discussion_name)

    def click_iv_clean_text(self):
        self.click_wait_button(self.iv_clean_text)

    def click_save(self):
        self.click_wait_button(self.save)



















































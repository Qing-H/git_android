# -*- coding:utf-8 -*-
import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config



#a发送成功
#判断依据：无“！”出现
def verify_send_success(test_evm):
    try:
        #bt = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_message_status")
        bt=test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_message_status")
    except Exception:
        return True
    return False
    # if test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/chat_message_status"):
    #     return False
    # else:
    #     return True

#b接受成功
#(主页验证)判断依据：等待5S，主页是否出现未读提示
def verify_recv_success(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i<time_interval_times:
        i = i+1
        try:
            bt = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/tv_unread_msg_count")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: not received in 5s")
    return False

#登录成功
#判断依据：等待5S，是否出现“会话”字样
# def verify_login(test_evm):
#     i = 0
#     while i < time_interval_times:
#         i = i + 1
#         try:
#             bt = test_evm.driver.find_element_by_name("会话")
#         except Exception:
#             sleep(time_interval)
#             continue
#         return True
#     print("Error: can't login")
#     return False
def verify_login(test_evm):

    try:
        bt = test_evm.driver.find_element_by_name("会话")
    except Exception:
        print("Error: can't login")
        return False
    return True


#退出登录成功
#判断依据：等待5S，是否出现“登录”字样
def verify_logoff(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_name("登录")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: can't logoff")
    return False

###########################################################
def verify_call_success(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_name("等待对方接听...")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: call fail")
    return False

def verify_answer_success(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/iv_mute")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: answer fail")
    return False

def verify_hangup_success(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_id("ctrip.android.xconnect:id/btn_start_call")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: hangup fail")
    return False

def verify_be_called(test_evm):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_name("邀请你语音聊天")
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: not be called")
    return False





















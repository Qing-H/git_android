# -*- coding:utf-8 -*-
import os
from time import sleep

import unittest

from appium import webdriver

from util import *
from res_id_list import *

# # 确认通话结束
# # 判断依据：不存在“通话状态”或者状态为正在结束通话。
# def verify_end(test_evm):
#     i = 0
#     while i<time_interval_times:
#         i = i+1
#         sleep(time_interval)
#         try:
#             tv_call_state = test_evm.driver.find_element_by_id(tv_call_state_id)
#             text = tv_call_state.text
#         except Exception as e :
#             return True
#         if (text == "正在结束通话") |(text == "对方拒绝接听") :
#             return True
#         else:
#             continue
#     return False

# 确认通话结束
# 判断依据：不存在“通话状态”或者状态为正在结束通话。
def verify_end(test_evm):
    i = 0
    while i<time_interval_times:
        i = i+1
        sleep(time_interval)
        try:
            iv_history = test_evm.driver.find_element_by_id(iv_history_id)
        except Exception as e :
            try:
                tv_call_state = test_evm.driver.find_element_by_id(tv_call_state_id)
                text = tv_call_state.text
            except:
                continue
            if (text == u"发来呼叫"):
                return True
            continue
        return True
    return False


# 确认有来电
# 判断依据：存在接听按钮
# 等待mid的时间，直到接听按钮出现
def verify_be_called(test_evm):
    i = 0
    while i<time_interval_times:
        i = i+1
        try:
            bt = test_evm.driver.find_element_by_id(btn_answer_id)
        except Exception:
            sleep(time_interval)
            continue
        return True
    print("Error: not been called in 10s")
    return False


# 确认当前没有来电
# 判断依据：不存在接听按钮
# 不做任何等待，只判断是否存在接听按钮。
def verfity_not_be_called(test_evm):
    try:
        bt = test_evm.driver.find_element_by_id(btn_answer_id)
    except Exception:
        return True
    return False


# 确认当前不在任何通话状态中
# 判断依据：不存在通话状态
# 不做任何等待，只判断是否存在通话状态。
def verify_not_in_anycall(test_evm):
    try:
        tv_call_state = test_evm.driver.find_element_by_id(tv_call_state_id)
    except Exception:
        # 不在任何通话中
        return True
    return False

# 确认当前在通话中
# 判断依据：存在通话状态
# 不做任何等待，只判断是否存在通话状态。
def verify_in_one_call(test_evm):
    try:
        tv_call_state = test_evm.driver.find_element_by_id(tv_call_state_id)
    except Exception:
        return False
    return True

# 确认当前不在任何通话状态中
# 判断依据：不存在通话状态
# 等待系统挂断时间65s，若确认不在通话中返回True，若超时返回False。
def verify_not_in_anycall_waited(test_evm):
    result_not_called = False
    i = 0
    while (i < time_interval_times_sys) | (not result_not_called):
        i = i + 1
        sleep(time_interval)
        result_not_called = verify_not_in_anycall(test_evm)
    return result_not_called

# 确认当前在通话状态中
# 判断依据：存在通话状态
# 等待系统挂断时间65s，若确认在通话中返回True，若超时返回False。
def verify_in_one_call_waited(test_evm):
    result_not_called = False
    i = 0
    while (i < time_interval_times_sys) | (not result_not_called):
        i = i + 1
        sleep(time_interval)
        result_not_called = verify_in_one_call(test_evm)
    return result_not_called



# 确认成功通话
# 判断依据：存在“通话状态”且“通话状态”为00:数字
def verify_in_call(test_evm):
    i = 0
    while i<time_interval_times:
        i = i+1
        sleep(time_interval)
        try:
            tv_call_state = test_evm.driver.find_element_by_id(tv_call_state_id)
            text = tv_call_state.text
        except Exception:
            sleep(time_interval)
            continue
        if text.find("00:"):
            return True
    return False

# 确认保持方成功保持
# 判断依据：静音按键不可用
def verify_hold(test_evm):
    bt = test_evm.driver.find_element_by_id(btn_mute_id)
    return not bt.is_enabled()

# 确认保持方成功保持
# 判断依据：静音按键不可用
def verify_hold_cancelled(test_evm):
    bt = test_evm.driver.find_element_by_id(btn_mute_id)
    return bt.is_enabled()

# 确认静音方成功静音
# 判断依据：静音按键被选中
def verify_mute(test_evm):
    bt = test_evm.driver.find_element_by_id(btn_mute_id)
    return bt.is_selected()

# 确认静音方成功静音
# 判断依据：静音按键不可用
def verify_mute_cancelled(test_evm):
    bt = test_evm.driver.find_element_by_id(btn_mute_id)
    return not bt.is_selected()
# -*- coding:utf-8 -*-
from res_id_list import *
from verify_items import *
from time import sleep

# input: test environment, button id
# output: None
# find a button in specific test enviorment test_evm, and click the button.
def click_button(test_evm, btn_id):
    bt = test_evm.driver.find_element_by_id(btn_id)
    bt.click()

# input: test environment, button id
# output: None
# wait a button till it exist, find a button in specific test enviorment test_evm, and click the button.
def click_wait_button(test_evm, btn_id):
    i = 0
    while i<time_interval_times:
        i = i+1
        if i == 500:
            raise ValueError("can't find elements")
        try:
            bt = test_evm.driver.find_element_by_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        bt.click()
        break

# input: test environment, button id
# output: None
# wait a button till it exist, find a button in specific test enviorment test_evm, and click the button.
def wait_button(test_evm, btn_id):
    i = 0
    while i < time_interval_times:
        i = i + 1
        if i == 500:
            raise ValueError("can't find elements")
        try:
            bt = test_evm.driver.find_element_by_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        return


# input: test environment, text id, content list
# output: None
# put content list into a EditText whose id is text_id.
def send_keys_login(test_evm, text_id, content_list):
    textfields = test_evm.driver.find_elements_by_class_name(text_id)
    content_len = len(content_list)
    i = 0
    while i<content_len:
        try:
            textfields[i].send_keys(content_list[i])
        except Exception as e:
            print("send keys failed @content list" + str(i))
        i = i + 1

# 输入：测试环境，要输入的文本框ID，待输入文本（多为电话号码）
# 输出：无
# 注意：只能输入一个字符串
def send_keys_dia(test_evm, text_id, phone_number):
    textfields = test_evm.driver.find_elements_by_id(text_id)
    textfields[0].send_keys(phone_number)




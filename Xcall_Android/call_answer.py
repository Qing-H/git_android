# -*- coding:utf-8 -*-
import os
from time import sleep

import unittest

from appium import webdriver

from util import *
from res_id_list import *

# make a call to the latest one
def make_call_history(test_evm):
    i = 0
    wait_button(test_evm, iv_history_id)
    while (i<time_interval_times):
        i = i+1
        try:
            history_field = test_evm.driver.find_element_by_id(iv_history_id)
            history_field.click()
            last_called = test_evm.driver.find_element_by_id(sl_history_item_id)
            last_called.click()
            return
        except Exception as e:
            print("element iv_history：")
            print(e)
            sleep(time_interval)

# make a call to the first people in contract
def make_call_contract(test_evm):
    contactField = test_evm.driver.find_element_by_id(iv_contacts_id)
    contactField.click()

    contact = test_evm.driver.find_element_by_id(sl_contact_item_id)
    contact.click()

    confirm = test_evm.driver.find_element_by_id(btn_call_id)
    confirm.click()

# use dial plate to make a call in test environment
# caution: only number, '*' and '#' are permitted, please don't input other character.
def make_call_dial(test_evm, phone_number):
    dia_field = test_evm.driver.find_element_by_id(iv_dialer_id)
    dia_field.click()
    i = 0
    number_len = len(phone_number)
    btn_to_click = ""
    while i<number_len:
        if (phone_number[i]=='*'):
            btn_to_click = Digit_id_raw + 'Star'
        elif (phone_number[i]=='#'):
            btn_to_click = Digit_id_raw + 'Hash'
        else:
            btn_to_click = Digit_id_raw + phone_number[i]
        if btn_to_click!="":
            click_button(test_evm,btn_to_click)
        btn_to_click = ""
        i = i + 1
    click_button(test_evm, btn_call_id)

# use dial plate to make a call in test environment
# caution: only number, '*' and '#' are permitted, please don't input other character.
def make_call_dial_address(test_evm, phone_number):
    dia_field = test_evm.driver.find_element_by_id(iv_dialer_id)
    dia_field.click()
    send_keys_dia(test_evm, address_id, phone_number)
    click_button(test_evm, btn_call_id)


# wait and answer the call, check it every once per second
def wait_and_answer_call(test_evm):
    sleep_time = 100 # wait for 100s, then timeout
    i = 0
    while i < sleep_time:
        sleep(1)
        i = i+1
        try:
            call_state = ""
            call_state_ele = test_evm.driver.find_element_by_id(tv_call_state_id)
            call_state = call_state_ele.text
        except Exception as e:
            # print(Exception, e)
            print("not get called yet, waiting...")
        if call_state == '发来呼叫':
            ans_btn = test_evm.driver.find_element_by_id(btn_answer_id)
            ans_btn.click()
            sleep(10)
            hang_off_btn = test_evm.driver.find_element_by_id(btn_hangup_after_id)
            hang_off_btn.click()
            sleep(10)
            break
        else:
            continue

    if i == sleep_time:
        print("timeOut...@wait_and_answer_call funciton.")


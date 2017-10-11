import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config
from utils.verify_items import *


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
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i<time_interval_times:
        i = i+1
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
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i < time_interval_times:
        i = i + 1
        try:
            bt = test_evm.driver.find_element_by_id(btn_id)
        except Exception:
            sleep(time_interval)
            continue
        return


def click_wait_button_byname(test_evm, name):
    i = 0
    time_interval = Config().get('time_interval')
    time_interval_times = Config().get('time_interval_times')
    while i<time_interval_times:
        i = i+1
        try:
            bt =test_evm.driver.find_element_by_name(name)
        except Exception:
            sleep(time_interval)
            continue
        bt.click()
        break




import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
from utils.verify_items import *
from utils.config import Config

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Base(object):

    def __init__(self, se_driver):
        self.driver = se_driver

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

    def click_wait_button_byclassname(test_evm, btn_id):
        i = 0
        time_interval = Config().get('time_interval')
        time_interval_times = Config().get('time_interval_times')
        while i<time_interval_times:
            i = i+1
            try:
                bt = test_evm.driver.find_element_by_class_name(btn_id)
            except Exception:
                sleep(time_interval)
                continue
            bt.click()
            break

    def click_wait_button_i(test_evm, btn_id,n):
        i = 0
        time_interval = Config().get('time_interval')
        time_interval_times = Config().get('time_interval_times')
        while i < time_interval_times:
            i = i + 1
            try:
                bt = test_evm.driver.find_elements_by_id(btn_id)
            except Exception:
                sleep(time_interval)
                continue
            bt[n].click()
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

    # def back(test_evm):
    #     btn_id = "android.widget.ImageButton"
    #     bt = test_evm.driver.find_element_by_id(btn_id)
    #     bt.click()

    def send(test_evm, btn_id,msg):
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
            bt.send_keys(msg)
            break

    def pics(test_evm,btn_id):
        for i in range(9):
            test_evm.driver.find_elements_by_id(btn_id)[i].click()

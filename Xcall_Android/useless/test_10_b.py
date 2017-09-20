# -*- coding:utf-8 -*-
""" 情境：A打给B，B接听，A操作转接C
    结果：C收到电话 """

import os
from time import sleep

import unittest

from appium import webdriver

from res_id_list import *
from util import *
from call_answer import *
from verify_items import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'D:/git/sample-code/sample-code/apps/xcall-android-v0.9-debug.apk'
        )
        desired_caps['appActivity'] = 'ctrip.android.xcall.ui.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'ctrip.android.xcall.ui.activity.HomeActivity'
        desired_caps['noReset'] = True

        # phone_b, the white redmi
        desired_caps['udid'] = device_b

        port_info = 'http://localhost:' + port_b + '/wd/hub'
        self.driver = webdriver.Remote(port_info, desired_caps)

    # 1. B长时间不应答
    # B等待100秒，不做任何动作
    def test_1_b(self):
        sleep(time_out_mid)

    def tearDown(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



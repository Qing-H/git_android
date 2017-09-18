# -*- coding:utf-8 -*-
""" 情境：A拨打B，1.B未接听
    结果：系统自动结束通话（目前默认30s） """

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


    # B先验证是否有电话进入，然后循环等待打入的电话消失
    def test_b_2(self):
        while verify_be_called(self):
            break
        while not verify_not_in_anycall(self):
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



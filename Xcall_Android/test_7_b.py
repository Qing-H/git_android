# -*- coding:utf-8 -*-
""" 情境6：A拨打B，1.B接听，2.AB通话中，A保持
    结果：A成功保持 """

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

    def b_answer(self):
        click_wait_button(self, btn_answer_id)


    def test_7_b(self):
        # 1.B接听
        self.b_answer()
        # 2.验证处于通话中
        result_incall = verify_in_call(self)
        self.assertTrue(result_incall)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



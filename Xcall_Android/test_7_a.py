# -*- coding:utf-8 -*-
""" 情境：1.A拨打B，B接听，2.AB通话中，3.A保持
    结果：4.A成功保持 """

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

        # phone_a, the golden redmi
        desired_caps['udid'] = device_a

        port_info = 'http://localhost:' + port_a + '/wd/hub'
        self.driver = webdriver.Remote(port_info, desired_caps)

    # 1.A拨打B
    # 注释：使用最近拨号方式拨打B
    def a_call_b(self):
        make_call_history(self)

    def a_hold(self):
        click_wait_button(self, btn_hold_id)

    def test_7_a(self):
        # 1.A拨打B
        self.a_call_b()
        # 2.验证AB通话中
        result = verify_in_call(self)
        self.assertTrue(result)
        # 3.A保持
        self.a_hold()
        # 4.验证成功保持
        result_end = verify_hold(self)
        self.assertTrue(result_end)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



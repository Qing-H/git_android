# -*- coding:utf-8 -*-
""" 情境：1.A拨打B，B未接听，2.A取消拨打
    结果：3.通话结束 """

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

    # 2.A取消拨打
    def a_cancelled(self):
        click_button(self, btn_hangup_before_id)
        result = verify_end(self)
        self.assertTrue(result)

    def test_1_a(self):
        self.a_call_b()
        sleep(5)
        self.a_cancelled()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)



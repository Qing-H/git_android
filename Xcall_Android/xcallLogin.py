# -*- coding:utf-8 -*-
import os
from time import sleep

import unittest

from appium import webdriver

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
            '../../../sample-code/apps/xcall-android-v0.9-debug.apk'
        )
        desired_caps['appActivity'] = 'ctrip.android.xcall.ui.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'ctrip.android.xcall.ui.activity.LoginActivity'
        desired_caps['noReset'] = True

        # phone1
        desired_caps['udid'] = 'e73af2057d53'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_login(self):
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")

        textfields[0].send_keys("13671746702")
        textfields[1].send_keys("123")

        bt = self.driver.find_element_by_id('ctrip.android.xcall:id/btn_login')
        bt.click()


    def ctest_to_client(self):
        a = 548.0 / 1080
        b = 1207.0 / 1920

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * a)
        y1 = int(y * b)
        self.driver.swipe(x1, y1, x1, y1, 1)

        self.driver.swipe(x, y, x, y, 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

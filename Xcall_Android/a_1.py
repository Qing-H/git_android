import os
from time import sleep

import unittest

from appium import webdriver

from res_id_list import *
from util import *
from call_answer import *
from verify_items import *

import time
from parametic import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Aphone_AndroidTests(ParametrizedTestCase):

    @classmethod
    def setUpClass(cls):
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

        desired_caps['timeout'] = 3000

        port_info = 'http://localhost:' + port_a + '/wd/hub'
        cls.driver = webdriver.Remote(port_info, desired_caps)
        cls.pipe_num = 1

    def a_call_b(self):
        make_call_history(self)

    # 2.A取消拨打
    def a_cancelled(self):
        click_button(self, btn_hangup_before_id)
        result = verify_end(self)
        self.assertTrue(result)

    def a_hangover(self):
        click_wait_button(self, btn_hangup_after_id)

    def a_answer(self):
        click_wait_button(self, btn_answer_id)

    def test_6_a(self):

        print("proc1 t6s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        self.a_call_b()
        sleep(2)
        #result = verify_in_call(self)
        #self.assertTrue(result)
        # 回到后台10s
        self.driver.keyevent(3)
        sleep(10)
        self.driver.find_elements_by_class_name("android.widget.FrameLayout")[20].click()
        # 2.验证AB通话中
        sleep(5)
        result = verify_in_call(self)
        self.assertTrue(result)

        self.a_hangover()
        print("do something @proc1")
        print("proc1 t6e rev ***:", self.param.recv())

#B在后台，A给B拨打电话，未接通，A回到后台，B接通，A返回APP验证通话中
    def test_7_a(self):
        print("do something @proc1")
        print("proc1 t6e rev ***:", self.param.recv())
        self.a_call_b()
        sleep(2)
        self.driver.keyevent(3)
        print("proc1 t6s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        sleep(10)
        self.driver.find_elements_by_class_name("android.widget.FrameLayout")[20].click()
        sleep(2)

        result = verify_in_call(self)
        self.assertTrue(result)
        self.a_hangover()

        print("do something @proc1")
        print("proc1 t6e rev ***:", self.param.recv())
    @classmethod
    def tearDownClass(cls):
        print("test a tear down")
        cls.driver.quit()

if __name__ == '__main__':

    suite_a = unittest.TestLoader().loadTestsFromTestCase(Aphone_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite_a)

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


class Bphone_AndroidTests(ParametrizedTestCase):
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
        desired_caps['udid'] = device_b

        desired_caps['timeout'] = 3000

        port_info = 'http://localhost:' + port_b + '/wd/hub'
        cls.driver = webdriver.Remote(port_info, desired_caps)
        cls.pipe_num = 1

    def a_call_b(self):
        make_call_history(self)

    # 2.A取消拨打
    def b_cancelled(self):
        click_button(self, btn_hangup_before_id)
        result = verify_end(self)
        self.assertTrue(result)

    def b_hangover(self):
        click_wait_button(self, btn_hangup_after_id)

    def b_answer(self):
        click_wait_button(self, btn_answer_id)

    def test_6_b(self):
        print("proc2 t6s rev ---:", self.param.recv())
        print("do something @proc2")

        # 1.B接听
        self.b_answer()
        # # 2.验证处于通话中
        result_incall = verify_in_call(self)
        self.assertTrue(result_incall)
        # # 3.验证通话结束
        # result_end = verify_end(self)
        # self.assertTrue(result_end)
        sleep(5)

        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_7_b(self):
        self.driver.keyevent(3)
        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        #sleep(2)

        print("proc2 t6s rev ---:", self.param.recv())
        print("do something @proc2")

        # 1.B接听
        self.b_answer()
        # # 2.验证处于通话中
        result_incall = verify_in_call(self)
        self.assertTrue(result_incall)
        sleep(5)
        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    @classmethod
    def tearDownClass(cls):
        print("test a tear down")
        cls.driver.quit()


if __name__ == '__main__':
    suite_a = unittest.TestLoader().loadTestsFromTestCase(Bphone_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite_a)

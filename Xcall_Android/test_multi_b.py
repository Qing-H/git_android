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


        desired_caps['udid'] = device_b

        port_info = 'http://localhost:' + port_b + '/wd/hub'
        cls.driver = webdriver.Remote(port_info, desired_caps)
        cls.pipe_num = 2

    def b_call_a(self):
        make_call_history(self)

    def b_hangup(self):
        click_wait_button(self, btn_reject_id)

    def b_answer(self):
        click_wait_button(self, btn_answer_id)

    def btest_1_b(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        # wait_button(self, tv_call_state_id)
        sleep(1)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    # def ctest_2_b(self):
    #     result_called = False
    #     while not result_called:
    #         result_called = verify_be_called(self)
    #         pass
    #     self.assertTrue(result_called)
    #
    #     while not verify_not_in_anycall(self):
    #         pass

    def btest_3_b(self):
        print("proc2 t3s rev ---:", self.param.recv())
        print("do something @proc2")
        sleep(2)
        # print("test_3_b:starting....")
        self.b_hangup()
        # result = verify_end(self)
        # self.assertTrue(result)
        # print("test_3_b:ending....")

        print("proc2 t3e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)


    def btest_4_b(self):
        print("proc2 t4s rev ---:", self.param.recv())
        print("do something @proc2")
        sleep(2)
        # 1.B接听
        self.b_answer()
        # result_incall = verify_in_call(self)
        # self.assertTrue(result_incall)
        # print("验证通话中ok了")
        # 3.验证通话结束
        # result_end = verify_end(self)
        # self.assertTrue(result_end)
        # print("test_4_b:ending....")

        print("proc2 t4e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def btest_5_b(self):
        print("proc2 t5s rev ---:", self.param.recv())
        print("do something @proc2")
        sleep(2)
        self.b_answer()
        # 2.验证处于通话中
        # result_incall = verify_in_call(self)
        # self.assertTrue(result_incall)
        # 3.验证通话结束
        # result_end = verify_end(self)
        # self.assertTrue(result_end)
        # print("test_5_b:ending....")

        print("proc2 t5e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.param.recv()
        self.param.send(self.pipe_num)



    def btest_6_b(self):
        print("proc2 t6s rev ---:", self.param.recv())
        print("do something @proc2")

        # 1.B接听
        self.b_answer()
        # # 2.验证处于通话中
        result_incall = verify_in_one_call(self)
        self.assertTrue(result_incall)
        # # 3.验证通话结束
        # result_end = verify_end(self)
        # self.assertTrue(result_end)
        sleep(5)

        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def btest_7_b(self):
        self.driver.keyevent(3)
        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        #sleep(2)

        print("proc2 t6s rev ---:", self.param.recv())
        print("do something @proc2")

        # 1.B接听
        self.b_answer()
        # # 2.验证处于通话中
        result_incall = verify_in_one_call(self)
        self.assertTrue(result_incall)
        sleep(5)
        print("proc2 t6e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.param.recv()
        self.param.send(self.pipe_num)

    def test_all_b(self):
        for i in range(100):
            self.btest_1_b()
            self.btest_3_b()
            self.btest_4_b()
            self.btest_5_b()
            self.btest_6_b()
            self.btest_7_b()

    @classmethod
    def tearDownClass(cls):
        print("test b tear down")
        cls.driver.quit()

if __name__ == '__main__':
    pipe = 2
    suite_b = unittest.TestLoader().loadTestsFromTestCase(Bphone_AndroidTests(pipe))
    unittest.TextTestRunner(verbosity=2).run(suite_b)
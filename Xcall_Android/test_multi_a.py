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

    # 1.A拨打B
    # 注释：使用最近拨号方式拨打B
    def a_call_b(self):
        make_call_history(self)

    # 2.A取消拨打
    def a_cancelled(self):
        click_button(self, btn_hangup_before_id)
        result = verify_end(self)
        self.assertTrue(result)

    def a_hangover(self):
        click_wait_button(self, btn_hangup_after_id)

    # A点击保持按钮
    def a_hold(self):
        click_wait_button(self, btn_hold_id)

    # A点击静音按钮
    def a_mute(self):
        click_wait_button(self, btn_mute_id)

    def atest_1_a(self):
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.a_call_b()
        self.a_cancelled()

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

    # def ctest_2_a(self):
    #     self.a_call_b()
    #     sleep(time_out_sys_hangup)
    #     result = verify_end(self)
    #     self.assertTrue(result)

    def atest_3_a(self):
        print("proc1 t3s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        self.a_call_b()
        # while (not verify_not_in_anycall(self)) & (i<time_interval_times):
        #     i = i+1

        print("do something @proc1")
        print("proc1 t3e rev ***:", self.param.recv())

    def atest_4_a(self):
        print("proc1 t4s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        # 1.A拨打B
        self.a_call_b()
        print("do something @proc1")
        print("proc1 t4e rev ***:", self.param.recv())
        sleep(1)
        # 2.验证AB通话中
        result = verify_in_one_call(self)
        self.assertTrue(result)  # 4.验证通话结束
        # 3.A挂断
        self.a_hangover()

        # result_end = verify_end(self)
        # self.assertTrue(result_end)
        # sleep(1)



    def atest_5_a(self):

        print("proc1 t5s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        self.a_call_b()
        print("do something @proc1")
        print("proc1 t5e rev ***:", self.param.recv())

        sleep(1)
        self.a_hold()
        # 4.验证成功保持
        result_hold = verify_hold(self)
        self.assertTrue(result_hold)
        # 5.A取消保持
        self.a_hold()
        # 6.A取消保持成功
        result_hold_cancelled = verify_hold_cancelled(self)
        self.assertTrue(result_hold_cancelled)
        # 7.A挂断
        self.a_hangover()
        # # 8.验证通话结束
        # result_end = verify_end(self)
        # self.assertTrue(result_end)


        self.param.send(self.pipe_num)
        self.param.recv()




# A给B拨打电话，B接通后，A退到后台10S，返回APP，验证通话依然存在
    def atest_6_a(self):

        print("proc1 t6s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        self.a_call_b()
        sleep(2)
        #result = verify_in_one_call(self)
        #self.assertTrue(result)
        # 回到后台10s
        self.driver.keyevent(3)
        sleep(10)
        self.driver.find_elements_by_class_name("android.widget.FrameLayout")[20].click()
        # 2.验证AB通话中
        sleep(5)
        result = verify_in_one_call(self)
        self.assertTrue(result)

        self.a_hangover()
        print("do something @proc1")
        print("proc1 t6e rev ***:", self.param.recv())


 #B在后台，A给B拨打电话，未接通，A回到后台，B接通，A返回APP验证通话中
    def atest_7_a(self):
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

        result = verify_in_one_call(self)
        self.assertTrue(result)
        self.a_hangover()

        print("do something @proc1")
        print("proc1 t6e rev ***:", self.param.recv())

        self.param.send(self.pipe_num)
        self.param.recv()

    def test_all_a(self):
        for i in range(100):
            print("Start running test" + "---------------------"+ str(i))
            self.atest_1_a()
            self.atest_3_a()
            self.atest_4_a()
            self.atest_5_a()
            self.atest_6_a()
            self.atest_7_a()


    @classmethod
    def tearDownClass(cls):
        print("test a tear down")
        cls.driver.quit()
if __name__ == '__main__':
    pipe = 1
    suite_a = unittest.TestLoader().loadTestsFromTestCase(Aphone_AndroidTests(pipe))
    unittest.TextTestRunner(verbosity=2).run(suite_a)
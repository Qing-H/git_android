# a发送消息给b：hello
# b验证接收到消息，并发送消息给a：hi
from call_answer import *
from verify_items import *
from util import *
import time
from parametic import *
import unittest
from appium import webdriver
import os
from parametic import *
from selenium import webdriver
from parametrizedTestCase import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class A_AndroidTests(ParametrizedTestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'D:/git/sample-code/sample-code/apps/xconnect-android-v0.4.0-debug.apk'
        )
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://localhost:4763/wd/hub', desired_caps)
        self.pipe_num = 1



    def test_sendmsg(self):
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        time.sleep(1)
        # el = self.driver.find_element_by_id("ctrip.android.xconnect:id/conversation")
        # el.click()
        # el = self.driver.find_element_by_id("ctrip.android.xconnect:id/rl_item_view")
        # el.click()
        # input = self.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
        # #el.click()
        #
        # input.send_keys("hello")
        # send = self.driver.find_element_by_id("ctrip.android.xconnect:id/btn_send_message")
        # send.click()

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

        click_wait_button(self, "ctrip.android.xconnect:id/conversation")
        click_wait_button(self, "ctrip.android.xconnect:id/rl_item_view")
        input = self.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
        # el.click()

        input.send_keys("hello")
        send = self.driver.find_element_by_id("ctrip.android.xconnect:id/btn_send_message")
        send.click()
        #self.param.send(self.pipe_num)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    pipe = 1
    suite = unittest.TestLoader().loadTestsFromTestCase(A_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)






















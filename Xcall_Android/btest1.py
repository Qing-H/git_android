# a发送消息给b：hello
# b验证接收到消息，并发送消息给a：hi

import unittest
from appium import webdriver
import os
from util import *
from selenium import webdriver
from parametrizedTestCase import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class B_AndroidTests(ParametrizedTestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'D:/git/sample-code/sample-code/apps/xconnect-android-v0.4.0-debug.apk'
        )
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://localhost:4773/wd/hub', desired_caps)
        self.pipe_num = 2

    def test_rcvmsg(self):
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        time.sleep(5)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        click_wait_button(self, "ctrip.android.xconnect:id/conversation")
        click_wait_button(self, "ctrip.android.xconnect:id/rl_item_view")
        msg = ""
        # el = self.driver.find_element_by_id("ctrip.android.xconnect:id/conversation")
        # el.click()
        # el = self.driver.find_element_by_id("ctrip.android.xconnect:id/rl_item_view")
        # el.click()
        # msg_el = self.driver.find_element_by_id("ctrip.android.xconnect:id/chat_text")
        #self.param.recv(self.pipe_num)
        msg_el = self.driver.find_elements_by_name("hello")
        # if msg == 'hello':
        if msg_el:
            el = self.driver.find_element_by_id("ctrip.android.xconnect:id/chat_input")
            # el.click()
            el.send_keys("hi")
            send = self.driver.find_element_by_id("ctrip.android.xconnect:id/btn_send_message")
            send.click()
        else:
            print("wrong!")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    pipe = 2
    suite = unittest.TestLoader().loadTestsFromTestCase(B_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)






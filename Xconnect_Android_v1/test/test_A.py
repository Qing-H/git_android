import os
from time import sleep
from appium import webdriver
from utils.HTMLTestRunner import HTMLTestRunner
from utils.parametic import *
from utils.util import *
#from utils.verify_items import *
from utils.config import Config
from pages.ConversionPage import Conversion
from appium.webdriver.common.touch_action import TouchAction
from BasePage import Base
from pages.ContactsPage import Contacts


from parametic import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class A_ContactsPageTests(ParametrizedTestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        device_a =Config().get('device_a')
        path = Config().get('path')
        url = Config().get('url')
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(path)
        desired_caps['noReset'] = True
        desired_caps['udid'] = device_a
        desired_caps['timeout'] = 3000
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        cls.driver = webdriver.Remote(url, desired_caps)
        cls.pipe_num = 1


# A拨打B，B未接听，A挂断
    def test_1_a_call_b(self):
        contacts_page = Contacts(self.driver)
        contacts_page.click_contacts()
        #contacts_page.click_group_name_1()
        contacts_page.click_friends_name_4()
        self.param.recv()

        contacts_page.click_btn_start_call()
        sleep(2)
        result = verify_call_success(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)
        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())
        contacts_page.click_iv_hangup_calling()
        result = verify_hangup_success(self)
        self.assertTrue(result)


# A拨打B，B未接听，B挂断
    def test_2_a_call_b(self):
        contacts_page = Contacts(self.driver)
        contacts_page.click_btn_start_call()
        sleep(2)
        result = verify_call_success(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

# A拨打B，B接听，A挂断
    def test_3_a_call_b(self):
        contacts_page = Contacts(self.driver)
        contacts_page.click_btn_start_call()
        sleep(2)
        result = verify_call_success(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())
        contacts_page.click_iv_hangup()
        result = verify_hangup_success(self)
        self.assertTrue(result)

# A拨打B，B接听，B挂断
    def test_4_a_call_b(self):
        contacts_page = Contacts(self.driver)
        contacts_page.click_btn_start_call()
        sleep(2)
        result = verify_call_success(self)
        self.assertTrue(result)
        print("proc1 t1s send***: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

        print("do something @proc1")
        print("proc1 t1e rev ***:", self.param.recv())

    @classmethod
    def tearDownClass(cls):
        print("test a tear down")
        cls.driver.quit()

if __name__ == '__main__':
    pipe = 1
    suite_a = unittest.TestLoader().loadTestsFromTestCase(A_ContactsPageTests(pipe))
    unittest.TextTestRunner(verbosity=2).run(suite_a)
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

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class B_ContactsPageTests(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        device_b =Config().get('device_b')
        path = Config().get('path')
        url2 = Config().get('url2')
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(path)
        desired_caps['noReset'] = True
        desired_caps['udid'] = device_b
        desired_caps['timeout'] = 3000
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        cls.driver = webdriver.Remote(url2, desired_caps)
        cls.pipe_num = 2


    def test_1_b(self):
        contacts_page = Contacts(self.driver)
        contacts_page.click_contacts()
        #contacts_page.click_group_name_1()
        contacts_page.click_friends_name_1()

        self.param.send(self.pipe_num)
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        result = verify_be_called(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)



    def test_2_b(self):
        contacts_page = Contacts(self.driver)
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")
        contacts_page.click_iv_hangup_called()

        result = verify_hangup_success(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_3_b(self):
        contacts_page = Contacts(self.driver)
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        result = verify_be_called(self)
        self.assertTrue(result)

        contacts_page.click_iv_answer_called()
        result = verify_answer_success(self)
        self.assertTrue(result)

        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    def test_4_b(self):
        contacts_page = Contacts(self.driver)
        print("proc2 t1s rev ---:", self.param.recv())
        print("do something @proc2")

        result = verify_be_called(self)
        self.assertTrue(result)

        contacts_page.click_iv_answer_called()
        result = verify_answer_success(self)
        self.assertTrue(result)

        contacts_page.click_iv_hangup()
        result = verify_hangup_success(self)
        self.assertTrue(result)


        print("proc2 t1e send---: %s" % (self.pipe_num))
        self.param.send(self.pipe_num)

    @classmethod
    def tearDownClass(cls):
        print("test a tear down")
        cls.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(B_ContactsPageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
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

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class A_ConversionPageTests(ParametrizedTestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        path = Config().get('path')
        url = Config().get('url')
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(path)
        desired_caps['noReset'] = True
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        cls.driver = webdriver.Remote(url, desired_caps)

    def test_a_send_msg(self):
        msg_1 = Config().get('msg_1')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_rl_item_view_i(0)
        conversion_page.click_send(msg_1)
        conversion_page.click_btn_send_message()
        conversion_page.click_back_ImageButton()

    def test_b_send_pic(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_rl_item_view_i(0)
        conversion_page.click_chat_btn_more()
        conversion_page.click_button_img()
        conversion_page.click_pics()
        conversion_page.click_done()
        conversion_page.click_back_ImageButton()

    def test_c_add_friends1(self):
        friends_name_2 = Config().get('friends_name_2')
        friends_name_3 = Config().get('friends_name_3')
        group_name_2_1 = Config().get('group_name_2_1')
        msg_2 = Config().get('msg_2')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_action_plus()
        conversion_page.click_search(friends_name_2)
        conversion_page.click_container_i(1)
        conversion_page.click_search(group_name_2_1)
        conversion_page.click_search(friends_name_3)
        conversion_page.click_tv_start_chat()
        conversion_page.click_send(msg_2)
        conversion_page.click_btn_send_message()
        conversion_page.click_back_ImageButton()

    def test_d_rename1(self):
        new_group_1 = Config().get('new_group_1')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_old_group_1()
        conversion_page.click_action_settings()
        conversion_page.click_tv_discussion_name()
        conversion_page.click_iv_clean_text()
        conversion_page.click_send_et_name(new_group_1)
        conversion_page.click_save()
        conversion_page.click_back_ImageButton()
        conversion_page.click_back_ImageButton()

    def test_e_add_friends2(self):
        friends_name_2 = Config().get('friends_name_2')
        friends_name_3 = Config().get('friends_name_4')
        group_name_2_1 = Config().get('group_name_2_1')
        msg_2 = Config().get('msg_3')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_search(friends_name_2)
        conversion_page.click_action_settings()
        conversion_page.click_riv_avatar_i(1)
        conversion_page.click_container_i(1)
        conversion_page.click_search(group_name_2_1)
        conversion_page.click_search(friends_name_3)
        conversion_page.click_tv_start_chat()
        conversion_page.click_send(msg_2)
        conversion_page.click_btn_send_message()
        for i in range(3):
            conversion_page.click_back_ImageButton()

    def test_f_rename2(self):
        new_group_2 = Config().get('new_group_2')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_old_group_2()
        conversion_page.click_action_settings()
        conversion_page.click_tv_discussion_name()
        conversion_page.click_iv_clean_text()
        conversion_page.click_send_et_name(new_group_2)
        conversion_page.click_save()
        conversion_page.click_back_ImageButton()
        conversion_page.click_back_ImageButton()

    def test_g_delete_friends(self):
        friends_name_2 = Config().get('friends_name_2')
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_new_group_1()
        conversion_page.click_action_settings()
        conversion_page.click_riv_avatar_i(4)
        conversion_page.click_search(friends_name_2)
        conversion_page.click_tv_start_chat()
        conversion_page.click_back_ImageButton()
        conversion_page.click_back_ImageButton()

    def test_h_quit_group(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        conversion_page.click_new_group_2()
        conversion_page.click_action_settings()
        conversion_page.click_quit_discussion()
        conversion_page.click_lef_btn()
        conversion_page.click_quit_discussion()
        conversion_page.click_right_btn()

    def test_i_press_delete(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        item = self.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[1]
        TouchAction(self.driver).press(item).wait(1000).perform()  # 按住应用图标不放
        conversion_page.click_button_name_1()

    def test_j_press_stick(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        item = self.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[2]
        TouchAction(self.driver).press(item).wait(1000).perform()  # 按住应用图标不放
        conversion_page.click_button_name_2()

    def test_k_press_unstick(self):
        conversion_page = Conversion(self.driver)
        conversion_page.click_conversation()
        item = self.driver.find_elements_by_id("ctrip.android.xconnect:id/rl_item_view")[0]
        TouchAction(self.driver).press(item).wait(1000).perform()  # 按住应用图标不放
        conversion_page.click_button_name_3()




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ == '__main__':
#     report = "D:\study\Test_Framework\\report" + '\\report.html'
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='Xconnect Test Report', description='修改html报告')
#         suite = unittest.TestLoader().loadTestsFromTestCase(A_ConversionPageTests)
#         runner.run(suite)

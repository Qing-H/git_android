# -*- coding:utf-8 -*-
# login test, use xuelei's account
# env:
# desired_caps['appActivity'] = 'ctrip.android.xcall.ui.activity.SplashActivity'
# desired_caps['appWaitActivity'] = 'ctrip.android.xcall.ui.activity.LoginActivity'
def ctest_login(self):
    textfields = self.driver.find_elements_by_class_name("android.widget.EditText")

    textfields[0].send_keys("13671746702")
    textfields[1].send_keys("123")

    bt = self.driver.find_element_by_id('ctrip.android.xcall:id/btn_login')
    bt.click()
# -*- coding:utf-8 -*-
# 整体通话超时时间设置
time_out_small = 5
time_out_mid = 15
time_out_large = 20
time_out_xlarge = 30
time_out_sys_max = 65

time_interval = 0.001
time_interval_times = time_out_small / time_interval
time_interval_times_mid = time_out_mid/time_interval
time_interval_times_large = time_out_large/time_interval
time_interval_times_xlarge = time_out_xlarge/time_interval
time_interval_times_sys = time_out_sys_max/time_interval


# 两个手机使用的端口
port_a = '4743'
# port_b = '4733'
#port_c = '4733'
# port_c = '4753'
port_b = '4753'
phone_num_a = '15951906477'
# phone_num_b = '18566266630'
#phone_num_c = '18566266630'
# phone_num_c = '15951906477'
phone_num_b = '15951906479'
#device_a = 'e73af2057d53'
device_b = '174ac0047d43' #白
#device_c = '174ac0047d43'
# device_c = 'd4fdce7'
device_a = 'd4fdce7'  #黑米

apk = 'D:/git/sample-code/sample-code/apps/xcall-android-v0.9-debug.apk'



# 系统自动挂断时间
time_out_sys_hangup = 32
time_out_sys_max = 65

# 全屏，小窗切换
btn_fullscreen_id = 'ctrip.android.xcall:id/btn_fullscreen'
# 联系人列表
ll_user_info_id = 'ctrip.android.xcall:id/ll_user_info'

# 角色：拨号方/被拨号方
# 情境：接通通话后
# 取值：00:12，发来呼叫，正在呼叫...，正在结束通话
tv_call_state_id ='ctrip.android.xcall:id/tv_call_state'


# 角色：拨号方/被拨号方
# 情境：接通通话后
# 1.拨号盘
btn_dial_id = 'ctrip.android.xcall:id/btn_dial'
# 2.保持
btn_hold_id = 'ctrip.android.xcall:id/btn_hold'
# 3.静音
btn_mute_id = 'ctrip.android.xcall:id/btn_mute'
# 4.免提
btn_speaker_id = 'ctrip.android.xcall:id/btn_speaker'
# 5.转接
btn_change_id = 'ctrip.android.xcall:id/btn_change'
# 6.添加通话
btn_add_id = 'ctrip.android.xcall:id/btn_add'
# 7.挂断
btn_hangup_after_id = 'ctrip.android.xcall:id/btn_hangup_after'


# 角色：被拨号方
# 情境：在接通通话前
# 1.接听
btn_answer_id = 'ctrip.android.xcall:id/btn_answer'
# 2.挂断
btn_reject_id = 'ctrip.android.xcall:id/btn_reject'

# 角色：拨号方
# 环境：在接通通话前
btn_hangup_before_id = 'ctrip.android.xcall:id/btn_hangup_before'

# 1.首页：
iv_home_id = 'ctrip.android.xcall:id/iv_home'
# 2.最近通话：
iv_history_id = 'ctrip.android.xcall:id/iv_history'
# 最近通话人
sl_history_item_id = 'ctrip.android.xcall:id/sl_history_item'
# 3.联系人：
iv_contacts_id = 'ctrip.android.xcall:id/iv_contacts'
# 首个联系人
sl_contact_item_id = 'ctrip.android.xcall:id/sl_contact_item'
# 4.拨号盘：
iv_dialer_id = 'ctrip.android.xcall:id/iv_dialer'


# 页面：拨号盘
# 1.输入号码
address_id = 'ctrip.android.xcall:id/address'
# 2.数字输入
Digit_id_raw = 'ctrip.android.xcall:id/Digit'
Digit1_id = 'ctrip.android.xcall:id/Digit1'
Digit2_id = 'ctrip.android.xcall:id/Digit2'
Digit3_id = 'ctrip.android.xcall:id/Digit3'
Digit4_id = 'ctrip.android.xcall:id/Digit4'
Digit5_id = 'ctrip.android.xcall:id/Digit5'
Digit6_id = 'ctrip.android.xcall:id/Digit6'
Digit7_id = 'ctrip.android.xcall:id/Digit7'
Digit8_id = 'ctrip.android.xcall:id/Digit8'
Digit9_id = 'ctrip.android.xcall:id/Digit9'
DigitStar_id = 'ctrip.android.xcall:id/DigitStar'
DigitHash_id = 'ctrip.android.xcall:id/DigitHash'
# 3.拨号
btn_call_id = 'ctrip.android.xcall:id/btn_call'

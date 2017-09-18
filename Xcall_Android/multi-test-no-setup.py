import os
import multiprocessing

from time import sleep
from res_id_list import *

import unittest
from test_multi_a import *
from test_multi_b import *

def worker_1():
    test_script = "python test_multi_b.py"
    os.system(test_script)

def worker_2():
    test_script = "python test_multi_a.py"
    os.system(test_script)

def a_test():
    suite_a = unittest.TestLoader().loadTestsFromTestCase(Aphone_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite_a)

def b_test():
    suite_b = unittest.TestLoader().loadTestsFromTestCase(Bphone_AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite_b)


if __name__ == "__main__":
    i = 0
    max_times = 100
    while i<max_times:
        print("\nStart testing at No." + str(i) + ".............")
        p1 = multiprocessing.Process(target=a_test)
        p2 = multiprocessing.Process(target=b_test)

        p1.start()
        p2.start()

        # time_i = 0
        # while ((p1.is_alive()) | (p2.is_alive())) & (time_i<time_interval_times_xlarge):
        #     time_i = time_i+1
        #     sleep(time_interval)

        p1.join(time_out_sys_max)
        p2.join(time_out_sys_max)

        p1.terminate()
        p2.terminate()

        sleep(5)
        i = i + 1
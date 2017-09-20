import os
import multiprocessing

from time import sleep
from res_id_list import *


def worker_1(test_num):
    test_script = "python test_" + str(test_num) + "_a.py"
    os.system(test_script)

def worker_2(test_num):
    test_script = "python test_" + str(test_num) + "_b.py"
    os.system(test_script)

if __name__ == "__main__":
    i = 1
    test_num_max = 9
    while i<=test_num_max:
        if i==4:
            i = i + 1
        print("Start testing test" + str(i) + ".............")
        p1 = multiprocessing.Process(target=worker_1, args=(i,))
        p2 = multiprocessing.Process(target=worker_2, args=(i,))

        p1.start()
        sleep(1)
        p2.start()

        time_i = 0
        while ((p1.is_alive()) | (p2.is_alive())) & (time_i<time_interval_times_xlarge):
            time_i = time_i+1
            sleep(time_interval)

        p1.join(time_out_sys_max)
        p2.join(time_out_sys_max)
        p1.terminate()
        p2.terminate()
        sleep(5)
        i = i+1


# -*- coding:utf-8 -*-
import unittest
import multiprocessing
import time

from a_1 import *
from b_1 import *
from parametic import *


class TestOne(ParametrizedTestCase):
    def test_a(self):
        i = 1
        print("proc1 send***: %s" % (i))
        self.param.send(i)
        time.sleep(5)
        print("do something @proc1")
        print("proc1 rev ***:", self.param.recv())


class TestTwo(ParametrizedTestCase):
    def test_b(self):
        i = 2
        print("proc2 rev ---:", self.param.recv())
        print("do something @proc2")
        time.sleep(1)
        print("proc2 send---: %s" % (i))
        self.param.send(i)

def a_test(pipe):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(Aphone_AndroidTests, param=pipe))
    unittest.TextTestRunner(verbosity=2).run(suite)

def b_test(pipe):
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(Bphone_AndroidTests, param=pipe))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    i = 0
    max_times = 100
    while i<max_times:
        print("Start running test" + str(i) +"---------------------x1")
        pipe = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=a_test, args=(pipe[0],))
        p2 = multiprocessing.Process(target=b_test, args=(pipe[1],))

        p1.start()
        p2.start()

        p1.join(time_out_sys_max)
        p2.join(time_out_sys_max)

        i = i+1
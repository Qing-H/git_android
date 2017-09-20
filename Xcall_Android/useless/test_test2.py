#_*_coding:utf-8_*_
from multiprocessing import *

import os, time



def f(q, n):
    q.put([n,'hello'])
    




if __name__ == '__main__':
    #此queue不是直接导入的import Queue,这个是multiprocessing重新封装的
    q = Queue()
    #循环6个进程
    for i in range(5):
           p=Process(target=f, args=(q,i))
           p.start()
    #等待子进程完毕后在继续执行
    p.join()
    for i in range(q.qsize()):
         print(q.get())
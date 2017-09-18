import multiprocessing
import time

def proc1(pipe):
    while True:
        for i in range(10):
            print("proc1 send***: %s" %(i))
            pipe.send(i)
            print("111111111")
            #time.sleep(5)
            print("do something @proc1")
            print("proc1 rev ***:", pipe.recv())

def proc2(pipe):
    while True:
        for i in range(10):
            print("proc2 rev ---:", pipe.recv())
            print("do something @proc2")
            print("22222222222")
            #time.sleep(1)
            print("proc2 send---: %s" %(i))
            pipe.send(i)




def proc3(pipe):
    while True:
        print("PROC3 rev:", pipe.recv())
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    #p3 = multiprocessing.Process(target=proc3, args=(pipe[1],))

    p1.start()
    p2.start()
    #p3.start()

    p1.join()
    p2.join()
    #p3.join()
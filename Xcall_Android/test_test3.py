import multiprocessing
import time

def wait_for_event(e):
    print("wait_for_event: starting")
    e.wait()
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))
    e.clear()
    print("@lvyue e.clear(): e.is_set()->" + str(e.is_set()))

def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))
    e.set()
    print("wait_for_event_timeout: event is set")


def wait_for_event2(e):
    print("wait_for_event2: starting")
    e.wait()
    print("wairt_for_event2: e.is_set()->" + str(e.is_set()))

def wait_for_event_timeout2(e, t):
    print("wait_for_event_timeout2:starting")
    e.wait(t)
    print("wait_for_event_timeout2:e.is_set->" + str(e.is_set()))
    e.set()
    print("wait_for_event_timeout2: event is set")


if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = "block",
            target = wait_for_event,
            args = (e,))

    w2 = multiprocessing.Process(name = "non-block",
            target = wait_for_event_timeout,
            args = (e, 2))
    w1.start()
    w2.start()

    time.sleep(3)

    # e.set()
    # print("main: event is set")

    # w3 = multiprocessing.Process(name = "block",
    #         target = wait_for_event2,
    #         args = (e,))
    #
    # w4 = multiprocessing.Process(name = "non-block",
    #         target = wait_for_event_timeout2,
    #         args = (e, 2))
    # w3.start()
    # w4.start()
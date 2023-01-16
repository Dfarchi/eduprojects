import threading
import time

def a():
    print("start a")
    print(threading.current_thread().name)
    t = threading.Thread(target=d)
    print("end a")
    return t


def b():
    print("start b")
    time.sleep(1)
    print("end b")
    return a()


def c():
    print("start c")
    time.sleep(3)
    print("end c")


def d():
    print("start d")
    time.sleep(1)
    print("end d")


def e():
    print("start e")
    time.sleep(5)
    print("end e")


t = b()
t1 = threading.Thread(target=c, name="c")
t2 = threading.Thread(target=e, name="e")
t2.start()
t.start()

t2.join(timeout=2.0)
if t2.is_alive():
    t2.join()

t1.start()
t.join()
t1.join()
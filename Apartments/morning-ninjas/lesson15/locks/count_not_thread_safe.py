# run in colab
import datetime
from threading import Thread, Lock

lock = Lock()

def count(counter_l):
    with lock:
        for i in range(100_000):

            # lock.acquire()
            counter_l[0] += 1
            # lock.release()

# t1 lock.acquire()
# .........


#t2 lock.acquire()

# counter[0] 7

# t1 counter[0] = counter[0](6) + 1  #7
# t2 counter[0] = counter[0] (6) + 1 #7


#
# if __name__ == '__main__':
#     threads = []
#     counter_wrapper = [0]
#
#     for i in range(10):
#         threads.append(Thread(target=count, args=(counter_wrapper, )))
#         threads[-1].start()
#
#     for t in threads:
#         t.join()
#
#     print(counter_wrapper)



class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = [] #action
        self.lock = Lock()
        self.print_lock = Lock()
        self.trans_num = 0

    def deposit(self, amnt):
        with self.print_lock:
            print("strting")
        with self.lock:
            now = datetime.datetime.now()
            # locked
            self.balance += amnt
            # cs
            self.transactions.append("deposit")
        with self.print_lock:
            print("done")

if __name__ == '__main__':
    pass



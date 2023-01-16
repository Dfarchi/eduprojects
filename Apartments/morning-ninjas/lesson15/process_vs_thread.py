
# def add_to_count(count):
#     count[0] += 10
#
# if __name__ == '__main__':
#     n = [5]
#     add_to_count(n)
#     print(n[0])
# n = 5
#
# def add_to_count():
#     global n
#     n = n + 10
#
# if __name__ == '__main__':
#     add_to_count()
#     print(n)
# from threading import Thread
#
#
# def add_to_count(count_wrapper):
#     count_wrapper[0] += 10
#
# if __name__ == '__main__':
#     num_wrapper = [5]
#     t1 = Thread(target=add_to_count, args=(num_wrapper, ))
#     t2 = Thread(target=add_to_count, args=(num_wrapper, ))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num_wrapper)
from multiprocessing import Process


def add_to_count(count_wrapper):
    count_wrapper[0] += 10
    print(count_wrapper)

if __name__ == '__main__':
    num_wrapper = [5]
    t1 = Process(target=add_to_count, args=(num_wrapper, ))
    t2 = Process(target=add_to_count, args=(num_wrapper, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num_wrapper)
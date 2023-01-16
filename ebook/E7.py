import datetime
import math
from concurrent.futures import ProcessPoolExecutor, wait, as_completed


def fun_factor(num:int):
    return math.factorial(num)

big_nums = [[1550]*100]*100
if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    executor = ProcessPoolExecutor()
    futures = []
    for lst in big_nums:
        for num in lst:
            future = executor.submit(fun_factor, num)
            futures.append(future)
    end1 = datetime.datetime.utcnow()
    for future in as_completed(futures):
        print(future.result())
    end = datetime.datetime.utcnow()
    print(f"Time took for calaulting: {(end1 - start).total_seconds()}s---------------------------------------")
    print(f"Time took for all: {(end - start).total_seconds()}s---------------------------------------")

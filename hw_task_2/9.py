import functools
import time


def measureTime(f):
    @functools.wraps(f)
    def wrapper_measureTime(*args, **kwargs):
        start_time = time.time()
        r = f(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time-start_time
        print(f'Time of {f.__name__} execution is: {exec_time:.16f} seconds')
        return r
    return wrapper_measureTime

@measureTime
def sortByOrderNum(elems):
    sorted_elems = sorted(elems, key= lambda x: x[1])
    time.sleep(1)
    return sorted_elems

@measureTime
def mySleep(sleep_time):
    time.sleep(sleep_time)


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(f"Elements: {elements}\n")
print(f"Sorted Elements: {sortByOrderNum(elements)}")
mySleep(2)
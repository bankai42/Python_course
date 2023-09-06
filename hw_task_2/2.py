def printResult(f):
    def result(*args, **kwargs):
        r = f(*args, **kwargs)
        print(f'Result is: {r}')
        return r
    return result

@printResult
def getMultiples(arr, num):
    return list(filter(lambda x: x % num == 0, arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
num = 3
getMultiples(arr, num)
def printResult(f):
    def result(*args, **kwargs):
        r = f(*args, **kwargs)
        print(f'Result is: {r}')
        return r
    return result

@printResult
def getIntersection(first, second):
    return list(filter(lambda x: x in second, first))

list_1 = [1, 2,3,4,5]
list_2 = [2, 4, 6, 8]
getIntersection(list_1, list_2)
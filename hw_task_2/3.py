def printResult(f):
    def result(*args, **kwargs):
        r = f(*args, **kwargs)
        print(f'Result is: {r}')
        return r
    return result

@printResult
def getStrs(*args):
    return list(filter(lambda x: isinstance(x, str), args))

getStrs(1, 2, 3, 'str', 'cat', 'god', [], True)
def printResult(f):
    def result(*args, **kwargs):
        r = f(*args, **kwargs)
        print(f'Result is: {r}')
        return r
    return result

@printResult
def removeStop(arr, stop):
    return (list(filter(lambda x: x not in stop, arr)))

arr = ['cat', 'dog', 'Python', 'go', 'qwerty']
stop = ['Python', 'php', 'go', 'C']

removeStop(arr, stop)
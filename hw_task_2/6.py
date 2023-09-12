def checkReturnInt(f):
    def result(*args, **kwargs):
        r = f(*args, **kwargs)
        if type(r) != int:
            raise Exception('Type is not integer!')
    
    return result

@checkReturnInt
def getArg(arg):
    return arg

@checkReturnInt
def getSum(arg1, arg2):
    return arg1+arg2

#getArg(1)
#getArg([1,2,3])
getSum('cat', ' dog')
#getSum(1,2)




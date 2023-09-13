import functools

def rerunReturnInt(f):
    @functools.wraps(f)
    def result(*args, **kwargs):
        try:
            r = f(*args, **kwargs)
            if type(r) != int:
                raise Exception('Type is not integer!')
        except Exception as e:
            print(e)
            result(*args, **kwargs)
        else: return r  
    return result

@rerunReturnInt
def askConvert2Int(number):
    smth = input('convert to integer? (y/n): ')
    modified_number = number
    if smth == 'y':
        modified_number = int(number)
    return modified_number

@rerunReturnInt
def sumTwoInputs():
    input1 = float(input('First input: '))
    input1 = askConvert2Int(input1)
    input2 = float(input('Second input: '))
    input2 = askConvert2Int(input2)
    return input1 + input2

#askConvert2Int(1.2)
print(sumTwoInputs())
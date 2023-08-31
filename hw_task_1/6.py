def countPositiveNums(list):
    counter = 0
    for num in list:
        if num > 0:
            counter += 1
    return counter

print(str(countPositiveNums([1,2,3,4,5])))
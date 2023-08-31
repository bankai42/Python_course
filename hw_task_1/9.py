def factorial(num):
    fac = 1
    for i in range(1, num+1):
        fac *= i
    print(str(fac))

factorial(6)
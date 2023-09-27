import numpy as np


a = np.zeros(10)
for i in range(10):
    number = 0
    while number == 0:
        number = np.random.random()
    a[i] = number

print(a)
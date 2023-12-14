import numpy as np

arr = 384*np.ones(20)
print(arr)

X = [1,200,3,100]
for i, num in enumerate(X):
    if num > 1 and num < 20:
        X[i]=2*num

print(X)
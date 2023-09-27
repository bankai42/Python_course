import numpy as np

m = np.zeros((8,8))
#print(m)

d = np.diag(np.ones(8), k=0)
m = m + d

for i in range(2,8,2):
    d = np.diag(np.ones(8-i),k=i)
    m = m+d+d.T

print(m)
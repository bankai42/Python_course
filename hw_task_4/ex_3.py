import numpy as np

a = np.random.randint(0,10,size=(8,4),dtype=int)
b = np.random.randint(0,10,size=(4,2),dtype=int)
print('a:\n', a, '\n\nb:\n', b, '\n\na*b:\n', a@b)
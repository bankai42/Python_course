import numpy as np

def neural_network(input_vector, layer_size, last=False):
    x = np.size(input_vector)
    s = layer_size
    A = input_vector
    B = np.random.randint(0, 10, size=(s,x))

    C = B@A

    sum_vector = C#p.sum(C, axis=1)

    if last:
        sum_vector = np.maximum(sum_vector, 0)
    else:
        sum_vector = np.sin(sum_vector)
    return sum_vector, B


input_size = 5 
layer_size = 10
output_size = 5
input = np.random.randint(10, size=(input_size,1))

res1, B1 = neural_network(input, layer_size)
res2, B2 = neural_network(res1, layer_size)
res3, B3 = neural_network(res2, output_size, last=True)

print(res3)
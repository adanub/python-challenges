import numpy as np

def create_array_from_function(f, d, dtype=int):
    coords = np.indices(d)
    return f(*coords)

print(create_array_from_function(lambda i,j: (i - j)**2, [4, 4]))
# [[0. 1. 4. 9.]
#  [1. 0. 1. 4.]
#  [4. 1. 0. 1.]
#  [9. 4. 1. 0.]]
import numpy as np

def boundary_cropping(a, m):
    mask = np.argwhere(m)

    #min/max for each dimension in 2d matrix format, eg. [[x_min, x_max], [y_min, y_max], [z_min, z_max]]
    #formatting it this way makes iteration for any number of dimensions in following line simple
    bounds = np.column_stack((mask.min(axis=0), mask.max(axis=0))) 

    return a[tuple([slice(b[0], b[1] + 1) for b in bounds])]

#---------------------------------------
a1 = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,1,0,1,1], [0,0,0,0,0]])
a2 = np.array([[ [0,0,0], [0,1,0], [0,1,0] ], [ [0,0,0], [0,1,0], [0,0,0] ], [ [0,0,0], [0,1,0], [0,0,0] ]])

print(boundary_cropping(a1, a1 != 0))
# [[1 0 1 1]]
print(boundary_cropping(a2, a2 != 0))
# [[[1] [1]] [[1] [0]] [[1] [0]]]
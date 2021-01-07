import itertools
import numpy as np

#only works for 2d arrays (provided examples)
def coordinates_from_steps_2d(a, s, dtype=int):
    coords = [] #list of coordinates

    for y in range(0, len(a)):
        if y % s[0] == 0:
            for x in range(0, len(a[y])):
                if x % s[1] == 0:
                    c = [ y, x]
                    coords.append(c)

    return coords

#works for arrays with any dimensions
def coordinates_from_steps(a, s, dtype=int):
    coords = [] #list of coordinates

    #returns a coordinate for an array with any number of dimensions
    def get_coordinates_recursively(arr, c, depth):
        for i in range(0, len(arr)):
            if i % s[depth] == 0:
                coord = c.copy() #lists are mutable, and each loop is a different coordinate
                coord.append(i)
                if arr.ndim > 1: #there is another array nested inside
                    get_coordinates_recursively(arr[i], coord, depth + 1)
                else:
                    coords.append(coord)

    get_coordinates_recursively(a, [], 0)

    return coords

print(coordinates_from_steps(np.array([[1,2],[3,4]]), (1,1)))
# [[0 0]
#  [0 1]
#  [1 0]
#  [1 1]]

#print(coordinates_from_steps(np.array([[[1,2],[3,4]], [[5,6],[7,8]]]), (1,1,1)))

print(coordinates_from_steps(np.array([[1,2],[3,4]]), (1,2)))
# [[0 0]
#  [1 0]]
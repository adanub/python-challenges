
class RoundRobin():

    def __init__(self, l):
        self.__data = l
        self.__index = 0 #current index for iteration

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        while self.__index >= len(self.__data): #if index is more than number of items in data, loop back from the start
            self.__index -= len(self.__data)
        return self.__data[self.__index - 1]

    def __getitem__(self, key):
        while key >= len(self.__data): #if key is more than number of items in data, loop back from the start
            key -= len(self.__data)
        return self.__data[key]

    def __setitem__(self, key, val):
        while key >= len(self.__data): #if key is more than number of items in data, loop back from the start
            key -= len(self.__data)
        self.__data[key] = val

    def __delitem__(self, key):
        while key >= len(self.__data): #if key is more than number of items in data, loop back from the start
            key -= len(self.__data)
        self.__data.pop(key)
        if self.__index > key:
            self.__index -= 1 #moving index back by 1 if removed element was before index, to maintain iteration order

#---------------------------------------
rr = RoundRobin(["a", "b", "c", "d"])

for (_, v) in zip(range(4), rr):
    print(v)

print('---')

rr[0] = 'A'

for (_, v) in zip(range(3), rr):
    print(v)

print('---')

del rr[2]

for (_, v) in zip(range(10), rr):
    print(v)
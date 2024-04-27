for k in {"x": 1, "y":2}:
    print(k)


my_list=[4,5,6]
my_iter=iter(my_list)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


import os 
print(dir(os))
print(os.getcwd()) # current working directory



import sys
sys.path
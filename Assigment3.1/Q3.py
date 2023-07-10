# What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

#iterator in python help us to iterate through iterables sequntially

list=[2, 4, 6, 8, 10, 12, 14,16, 18, 20]

itr=iter(list)

for i in range(5):
    print(next(itr))


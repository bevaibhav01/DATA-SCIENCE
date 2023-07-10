# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.

# *args is used when we to pass n no. of arguments to function;

def test(*args):
    return args


l = test(1, 2, 3, 4, 5)
print(l)


# **kwargs is used when we want to return dictionary from number and want to
# and wants to pass n arguments

def test2(**kwargs):
    return kwargs


l1 = test2(v1=1, v2=2, v3=3)
print(l1)

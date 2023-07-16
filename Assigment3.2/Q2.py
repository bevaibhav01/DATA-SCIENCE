# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
# lambda and map functions.


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

fun = lambda a: a ** 2

ans1 = []

for i in l:
    ans1.append(fun(i))


def sqr(n):
    return n ** 2


ans2 = list(map(sqr, l))

print(ans2)
print(ans1)

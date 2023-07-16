# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
# filter function.
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

l1=list(filter(lambda x: x%2==0 and x%3==0 ,l))

print(l1)

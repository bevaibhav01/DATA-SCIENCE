# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# out odd numbers.

list=[x for x in range(1,101)]

oddList=[x for x in list if x%2==1]

print(oddList)
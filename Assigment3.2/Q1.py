# Q1. Create a python program to sort the given list of tuples based on integer value using a
# lambda function.
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

list=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

#to sort collection of complex use sorted() method
list=sorted(list , key=lambda player:player[1])

print(list)


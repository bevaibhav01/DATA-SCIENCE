# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.

# In Python, a generator function is a special type of function that returns an
# iterator object, which can be iterated over to generate a sequence of values.
# Unlike regular functions that use the return statement, generator functions use
# the yield statement to return a value while maintaining their internal state.
# This allows them to generate values on the fly, conserving memory and improving
# performance for large data sets or infinite sequences.

def fibo():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


list = fibo()

for i in range(10):
    print(next(list))

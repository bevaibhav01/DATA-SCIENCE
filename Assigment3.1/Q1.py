# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

#WE CREATE FUNCTION USING def keyword

def odd():
    list=[]
    for i in range(1,25):
        if(i%2==1):
            list.append(i)
    return list

l=odd()
print(l);


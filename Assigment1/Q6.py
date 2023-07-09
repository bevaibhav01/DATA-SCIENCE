# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

list = range(1, 26)

for i in list:
    if i % 3 ==0:
        print(i,"is divisible by 3")

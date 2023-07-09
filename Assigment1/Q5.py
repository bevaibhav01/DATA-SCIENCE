# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

a = int(input("number a"))
b = int(input("number b"))
count = 0
while a > 0:
    a = a - b
    count += 1

if a == 0:
    print(count)
else:
    print("not divisble")

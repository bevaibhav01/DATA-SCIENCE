# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

def isPalindrome(n):
    real=n
    rev=0

    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev==real

a=int(input("Enter the Number"));

print(isPalindrome(a))

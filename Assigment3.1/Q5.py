# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primeList():
    for i in range(1000):
        if isPrime(i):
            yield i

list=primeList()

for i in range(20):
    print(next(list))


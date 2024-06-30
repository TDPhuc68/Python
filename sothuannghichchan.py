import math


def isPrime(n):
    if n < 2:
        return False
    if n < 3:
        return True
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    n = input()
    if isPrime(int(n[-4::])):
        print("YES")
    else:
        print("NO")
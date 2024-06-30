def isPrime(n):
    if n == 1 : return False
    if n < 3 :
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a

test = int(input())
for i in range(test):
    n = int(input())
    k=0
    for i in range(n):
        if gcd(i,n) == 1 :
            k+=1
    if (isPrime(k)): print("YES")
    else : print("NO")


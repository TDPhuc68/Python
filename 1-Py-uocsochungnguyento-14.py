test = int(input())
def gcd(a,b):
    while b!= 0 :
        a,b = b, a%b
    return a
def nguyento(n):
    if n<= 1 :
        return False
    if n == 2 :return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5) +1,2):
        if n % i ==0 :
            return False
    return True
while test > 0:
    a,b = map(int,input().split())
    x = gcd(a,b)
    s=0
    while (x>0):
        i = x % 10
        s+=i
        x //=10

    if nguyento(s):
        print("YES")
    else :
        print("NO")
    test -= 1
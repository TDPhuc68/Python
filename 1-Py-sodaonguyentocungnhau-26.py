test = int(input())
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
while test > 0:
    n = input()
    m = n[::-1]
    if(gcd(int(m),int(n))==1):
        print("YES")
    else:
        print("NO")
    test -=1
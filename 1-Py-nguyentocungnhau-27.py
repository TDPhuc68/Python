import math
n,k = input().split()
def gcd(a,b):
    while b!=0:
        a,b =b,a%b
    return a
n= int(n)
k= int(k)
c = pow(10,k-1)
d = pow(10,k)
dem =0

for i in range(c,d):
        if (gcd(i,n) ==1 ):
            print(i,end=" ")
            dem +=1
            if dem % 10 ==0:
                print()

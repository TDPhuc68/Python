import math
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
l,r = list(map(int,input().split()))
for i in range(l,r+1):
    for j in range(i+1,r+1):
        for z in range(j+1,r+1):
            if(math.gcd(i,j)==1) and(math.gcd(j,z) ==1) and (math.gcd(z,i) == 1):
                print("(" + str(i) + ", " + str(j) + ", " + str(z) + ")",end="")
                print()


import math
test = int(input())
def nguyento(n):
    if n<2 : return False
    if n == 2 :return True
    for i in range(3,int(math.sqrt(n))) :
        if (n%i==0):
            return False
    return True

def uocso(n):
    dem =0
    for i in range(2,n):
        if (n%i ==0):
            dem +=1
    return dem
def xuly(n):
    souocso= uocso(n)
    so = 0
    for i in range(2, n):
        if nguyento(i):
            so += 1
    if (souocso> so):
        return True
    else :return False
while test >0:
    n = int(input())
    for i in range(n,10000000,1):
        if xuly(i)==True :
            print(i)
            break
    print()

    test -=1
test = int(input())
a = []
def check(n):
    for i in n:
        if int(i) % 2 == 1 :
            return False
    return True
num = 2
while num<=888:
    if check(str(num)) :
        tmp = str(num)
        a.append(int(tmp + tmp[::-1]))
    num +=2
while test >0 :
    n= int(input())
    for i in a :
        if i<n:
            print(i,end =' ')
    print()
    test -=1
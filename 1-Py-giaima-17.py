test = int(input())
while test >0:
    s= str(input())
    n= len(s)
    for i in range(1,n,2):
        cnt = int(s[i])
        for j in range (0,cnt):
            print(s[i-1],end='')
    print()

    test -=1
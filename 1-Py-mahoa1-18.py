
test = int(input())
while test > 0:

    s= input()
    x = len(s)
    cnt =1
    for i in range (1,x):

        if s[i] != s[i-1] :
            print(cnt,end='')
            print(s[i-1],end='')
            cnt=1
        else :
            cnt+=1
    print(cnt,end='')
    print(s[x-1])

    test -= 1
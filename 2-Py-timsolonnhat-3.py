test = int(input())

while test >0:
    s=input()
    s+="*"
    l = len(s)
    x=0
    res = -1
    for i in range(0,l-1):
        if s[i].isdigit():
            x = x*10 + int(s[i])
            if s[i+1].isalpha():
                res = max(res,x)
                x =0
    print(m)
    test -=1
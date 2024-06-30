test = int(input())
while test>0:
    n= input()
    n+="#"
    l = len(n)
    x=0
    res = 10 ** 19
    for i in range(0,l-1):
        if n[i].isdigit():
            x = x*10 + int(n[i])
            if n[i+1].isalpha():
                res = min(res,x)
                x =0
    print(res)
    test -=1

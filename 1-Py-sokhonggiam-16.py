test = int(input())
while test > 0:
    n= input()
    check =0
    for i in range(len(n)-1) :
        if n[i] > n[i+1] :

            check =1
            break
    if check == 1 : print("NO")
    else:
        print("YES")
    test -= 1
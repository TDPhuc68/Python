test = int(input())
while test > 0 :
    s1 =input()
    s2 = s1[::-1]
    check =0
    for i in range(1,len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            check =1
            break
    if check ==0:print("YES")
    else : print("NO")


    test -=1
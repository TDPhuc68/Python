test = int(input())
while(test > 0 ):
    s = input()
    k = len(s)
    if (s[0] == s[k-2] and s[1] ==s[k-1]):
        print("YES")
    else:
        print("NO")
    test -=1
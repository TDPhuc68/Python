n = int(input())
a = list(map(int, input().split()))

s =[]
for i in a :
    if len(s) == 0 :
        s.append(i)
    else :
        if (s[-1] + i) % 2 == 1:
            s.append(i)
        else :
            s.pop()
print(len(s))

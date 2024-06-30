n= int(input())
for i in range(n):
    s = input()

    for i in s:
        if(i != '4' and i != '7'):
            print("NO")
            break
    else : print("YES")
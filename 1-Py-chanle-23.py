test = int(input())
def check(n):
    sum=int(n[0])
    check =0
    for i in range(1,len(n)):
        sum += int(n[i])
        if abs(int(n[i]) - int(n[i-1])) != 2:
            check =1
            break
    if (sum % 10 == 0) and check ==0 :
        return "YES"
    else :
        return "NO"


while test >0:
    n = input()
    print(check(n))

    test -=1
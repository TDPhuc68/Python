a, k,n = map(int ,input().split())
b = k -a%k
check =0
for i in range(a+b,n+1,k):
    print(i-a,end =' ')
    check =1
if check ==0 : print("-1")
print()
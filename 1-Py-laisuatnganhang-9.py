from math import log,ceil
test = int(input())
while(test > 0):
    N,X,M = list(map(float,input().split()))
    X = X/100
    res = log(M/N) / log(1+X)
    year = ceil(res)
    print(year)
    test -= 1
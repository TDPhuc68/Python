import math
test =int(input())

while test > 0:
    n = int(input())
    sqr = int(math.sqrt(n))
    print("1",end=" ")
    for i in range(2,sqr+1):
        if n % i == 0 :
            dem =0
            while n% i==0:
                dem +=1
                n //=i
            print("* "+str(i)+ "^" +str(dem),end=" ")
            sqr = int(math.sqrt(n))
    if n>1:
        print("*",end=" ")
        print(str(n)+ "^" + str(1),end="")
    print()

    test -=1
n =int(input())

while n > 0 :
    m = input()
    X,Y,Z= input()
    max = 1000000
    x = X
    m = X 
        
    while(m>x):
        x+=x
        m +=Z
        m += (m-x)/X
        max(m,max)
print(m)
n-=1

        
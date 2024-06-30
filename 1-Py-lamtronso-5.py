n = int(input())
for i in range(n) :
    k =list(input())

    for j in range(len(k)-1,0,-1):
        if(int(k[j]) >= 5 and len(k)>1 ):
            k[j] = '0'
            k[j-1] = str(int(k[j-1])+1)
        elif(int(k[j]) < 5 and j!= 0):
            k[j] ='0'

    s = ''.join(k)
    print(s)

import math
n= int(input()) #khai báo số nguyên
a= list(map(int,input().split())) # khai báo danh sách dãy a[]
a.sort() # sắp xếp dãy từ thấp tới caooo

for i in range(n): 
    for j in range(i+1,n): 
        if math.gcd(a[i],a[j]) == 1: # sử dụng thuật toán tìm UCLN
            print(a[i],a[j])
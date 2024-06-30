#Viet 1 ham co chuc nang dao nguoc xau 
# xau = input()
# def daonguoc_xau(xau) :
#     return xau[::-1]

# xau1 = daonguoc_xau(xau)
# print(xau1)
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
  
# s = "Quantrimang"
  
# print("Chuỗi ban đầu là : ", end="")
# print(s)
  
# print("Chuỗi đã được đảo ngược (sử dụng vòng lặp) là : ", end="")
# print(reverse(s))
# tinhgiaithua
# n = int(input())
# def giaithua(n) :
#     s = 1
#     for i in range(2,n+1) :
#         s*= i
#     return s 

# a = giaithua(n)   
# print(a)    
#viet ham kiêm tra so nguyen to
# n= int(input())
# def snt(n) :
#     if(n <= 1 ) : 
#         return False
#     else :
#         for i in range(2,int(n**0.5)+1) :
#             if n % i == 0 :
#                 return False
#         return True 
       
# if(snt(n)) : print("la so nguyen to ")
# else : print(" k phai so nguyen to")
#Viet 1 hàm nhận 1 danh sách và trả về một danh sách mới với các phần tử riêng biệt từ danh sách đầu 
# ds=[1,2,3,3,3,3,4,5]
# def loaibods(ds) :
#     return list(set(ds))

# dsmoi = loaibods(ds)
# print(dsmoi) 
# c2:
# def ds(a) :
#     new_a = []
#     for n in a :
#         if n not in new_a :
#             new_a.append(n)
#     return new_a
# print(ds([1,2,3,3,3,4,5]) )      

n= int(input())
def tinh(n):
    s=0
    if (n%2==1) :
        
        for i in range(1,n+1,4):
            s+=1/i
        for i in range(3,n+1,4):
            s-=1/i
        return s 
    else :
         for i in range(2,n+1,4):
            s+=1/i
         for i in range(4,n+1,4):
            s-=1/i
         return s   
print( tinh(n))
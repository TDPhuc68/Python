class MatHang:
    tongtien =0
    def __init__(self,ma,ten,soluong,gia,chietkhau):
        self.ma = ma
        self.ten =ten
        self.soluong = soluong
        self.gia = gia
        self.chietkhau = chietkhau
        self.tongtien = self.gia * self.soluong -self.chietkhau

    def __str__(self):
        return self.ma + " " + self.ten +" "+str(self.soluong)+" "+str(self.gia)+" "+str(self.chietkhau)+" "+str(self.tongtien)

n= int(input())
a=[]
for i in range(n):
    ma =input()
    ten = input()
    soluong = int(input())
    gia = int(input())
    chietkhau=int(input())
    a.append(MatHang(ma,ten,soluong,gia,chietkhau))
a= sorted(a, key = lambda x : -x.tongtien)
    
for i in a:
    print(i)
    
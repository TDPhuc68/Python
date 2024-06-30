import math
class phanso:
    def __init__(self,tu ,mau):
        self.tu = tu
        self.mau = mau

    def toigian(self):
        gcd = math.gcd(self.tu,self.mau)
        self.tu //= gcd
        self.mau //=gcd
        return self
    def cong(self,a):
        mau = self.mau * a.mau // math.gcd(self.mau,a.mau)
        res = phanso(self.tu*mau // self.mau+a.tu*mau // a.mau,mau)
        return res.toigian()
a,b,c,d = list(map(int,input().split()))
A = phanso(a,b)
B = phanso(c,d)
C = A.cong(B)
print(str(C.tu) + '/' + str(C.mau))

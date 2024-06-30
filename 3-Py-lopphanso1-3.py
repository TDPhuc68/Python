import math
class phanso:
    def __init__(self,tu, mau):
        self.tu = tu
        self.mau = mau
    def rugon(self):
        GCD = math.gcd(self.tu,self.mau)
        self.tu //=GCD
        self.mau //=GCD
        return "{}/{}".format(self.tu,self.mau)
tu , mau = list(map(int,input().split()))
A = phanso(tu,mau)
print(A.rugon())
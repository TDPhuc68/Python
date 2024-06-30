class GiaoVien :
    def __init__(self,id,ten,ma,diemTH,diemCM):
        self.id ='GV0' +str(id)
        self.ten = ten
        self.ma =ma
        self.diemTH = diemTH
        self.diemCM = diemCM
        self.tongdiem =2*self.diemTH + self.diemCM
  
n= int(input())
tongdiem = 0
tenmon={}
a =[]
for i in range(n):
    ten = input()
    ma =input()
    diemTH =float(input())
    diemCM =float(input())
   

    if ma[0] =="A": tenmon = 'TOAN'
    elif ma[0] == "B" : tenmon ='LY'
    else: tenmon='HOA'
    if ma[1] == '1': tongdiem +=2
    elif ma[1] =='2':tongdiem +=1.5
    elif ma[1] == '3': tongdiem+=1
    

    a.append(GiaoVien(i+1,ten,ma,tenmon))
a =sorted(a, key = lambda x : -x.tongdiem)
for j in a:
    
    print(j)
    if tongdiem[j] < 18 :print("TRUNG TUYEN")
    else :print("LOAI")

    

n = input()
upper =0
for i in range(0,len(n)):
    if n[i].isupper():
        upper +=1
if(upper > len(n) -upper):
    print(n.upper())
else:
    print(n.lower())
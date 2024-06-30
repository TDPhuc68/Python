def xuly(K,S):
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    chuoikq =""
    for char in S:
        index = P.index(char)
        n_index = (index +K) % 28
        chuoikq += P[n_index]
    chuoi = chuoikq[::-1]
    return chuoi
while True:
    input_data = input().strip()
    if input_data == "0":
        break
    K,S = input_data.split()
    K = int(K)
    result= xuly(K,S)
    print(result)

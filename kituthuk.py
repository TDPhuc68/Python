def find_char(N, K):
    if N == 1:
        return 'A'
    
    middle = 2**(N-1)
    if K == middle:
        return chr(64 + N)  # Chữ cái thứ N theo bảng chữ cái Tiếng Anh in hoa
    elif K < middle:
        return find_char(N-1, K)
    else:
        return find_char(N-1, 2**N - K)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(find_char(N, K))
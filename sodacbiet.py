MOD = 10**9 + 7

def special_numbers(N, K):
    specials = set()
    specials.add(1)  # Thêm 1 vào tập hợp specials
    new_specials = set()
    new_specials.add(1)
    i = 1
    while len(specials) < K:
        power= pow(N, i, MOD)
        specials.add(power)
        for special in new_specials:
            specials.add((special + power) % MOD)
        # Cập nhật new_specials bằng specials
        new_specials = set(specials)
        i+=1


    sorted_specials = sorted(specials)
    return sorted_specials[K - 1] if K <= len(sorted_specials) else -1


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    result = special_numbers(N, K)
    print(result)
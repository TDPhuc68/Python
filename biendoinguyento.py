def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nearest_prime(n):
    lower_prime = n - 1
    upper_prime = n + 1
    while not is_prime(lower_prime):
        lower_prime -= 1
    while not is_prime(upper_prime):
        upper_prime += 1
    if n - lower_prime <= upper_prime - n:
        return lower_prime
    else:
        return upper_prime

def min_steps_to_primes(N, A):
    steps = 0
    for num in A:
        if not is_prime(num):
            nearest = nearest_prime(num)
            steps += abs(num - nearest)
    return steps

# Đọc số phần tử của dãy từ input
N = int(input())

# Đọc dãy số từ input và chuyển thành list
A = list(map(int, input().split()))

# Tính số bước cần thiết và in kết quả
result = min_steps_to_primes(N, A)
print(result)

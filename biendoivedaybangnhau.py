def min_steps_to_equalize(N, A):
    # Đếm số lần xuất hiện của mỗi giá trị trong dãy
    frequency = {}
    for num in A:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Chọn giá trị có số lần xuất hiện nhiều nhất
    target_value = max(frequency, key=frequency.get)
    
    # Tính tổng số bước cần để biến đổi tất cả các phần tử về giá trị được chọn
    total_steps = 0
    for num in A:
        total_steps += abs(num - target_value)
    
    return total_steps, target_value

# Đọc số lượng phần tử N từ input
N = int(input())

# Đọc dãy số từ input
A = list(map(int, input().split()))

# Tính số bước ít nhất và giá trị bằng nhau được chọn
min_steps, target_value = min_steps_to_equalize(N, A)

# In ra kết quả
print(min_steps, target_value)

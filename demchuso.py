def count_digits(A, B):
    # Khởi tạo danh sách lưu trữ tần suất xuất hiện của các chữ số từ 0 đến 9
    digit_count = [0] * 10
    
    # Chuyển A và B thành chuỗi
    str_A = str(A)
    str_B = str(B)
    
    # Lấy độ dài của chuỗi A và B
    len_A = len(str_A)
    len_B = len(str_B)
    
    # Tính tần suất xuất hiện của các chữ số từ 1 đến len_A - 1 trong A
    for i in range(1, len_A):
        digit = int(str_A[i])
        digit_count[digit] += (A // (10 ** (len_A - i))) * (10 ** (len_A - i - 1))
        if digit < int(str_A[i:]):
            digit_count[digit] += 10 ** (len_A - i - 1)
    
    # Tính tần suất xuất hiện của các chữ số từ 0 đến len_B - 1 trong B
    for i in range(len_B):
        digit = int(str_B[i])
        digit_count[digit] += (B // (10 ** (len_B - i))) * (10 ** (len_B - i - 1))
        if digit > int(str_B[i:]):
            digit_count[digit] += 10 ** (len_B - i - 1)
    
    # Tính tần suất xuất hiện của các chữ số từ len_A đến len_B
    for i in range(int(str_A[0]), int(str_B[0]) + 1):
        digit_count[i] += 1 if len_A == len_B else 0
    
    return digit_count

# Đọc số lượng bộ test
T = int(input())

# Với mỗi bộ test
for _ in range(T):
    A, B = map(int, input().split())
    
    # Gọi hàm để đếm số lần xuất hiện của các chữ số từ A đến B
    frequency = count_digits(A, B)
    
    # In ra kết quả
    print(*frequency)

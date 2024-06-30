def calculate_attendance_score(attendance_record):
    # Khởi tạo điểm chuyên cần ban đầu
    score = 10

    # Duyệt qua từng ký tự trong dữ liệu điểm danh
    for char in attendance_record:
        if char == 'v':  # Nếu vắng
            score -= 2
        elif char == 'm':  # Nếu đến muộn
            score -= 1
    
    # Đảm bảo điểm chuyên cần không âm
    score = max(0, score)

    return score

# Đọc số lượng sinh viên từ input
n = int(input())

# Khởi tạo danh sách sinh viên
students = []

# Đọc thông tin của từng sinh viên và lưu vào danh sách
for _ in range(n):
    student_id = input()
    student_name = input()
    student_class = input()
    students.append((student_id, student_name, student_class))

# Đọc dữ liệu điểm danh và tính điểm chuyên cần cho từng sinh viên
for i in range(n):
    student_id, student_name, student_class = students[i]
    attendance_record = input().strip()
    attendance_score = calculate_attendance_score(attendance_record)
    
    # In ra thông tin điểm chuyên cần của sinh viên
    print(student_id, student_name, student_class, attendance_score, end=' ')
    
    # Kiểm tra và in ghi chú nếu có
    if attendance_score == 0:
        print("KDDK")
    else:
        print()


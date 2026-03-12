import math

# Nhập chuỗi
s = input("Nhập chuỗi số (cách nhau bằng ;): ")

# Tách chuỗi thành danh sách số
numbers = [int(x.strip()) for x in s.split(";")]

# In từng số
print("Các số:")
for num in numbers:
    print(num)

# Đếm số chẵn
even_count = sum(1 for num in numbers if num % 2 == 0)

# Đếm số âm
negative_count = sum(1 for num in numbers if num < 0)

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Đếm số nguyên tố
prime_count = sum(1 for num in numbers if is_prime(num))

# Tính trung bình
average = sum(numbers) / len(numbers)

# In kết quả
print("Số chẵn:", even_count)
print("Số âm:", negative_count)
print("Số nguyên tố:", prime_count)
print("Giá trị trung bình:", average)
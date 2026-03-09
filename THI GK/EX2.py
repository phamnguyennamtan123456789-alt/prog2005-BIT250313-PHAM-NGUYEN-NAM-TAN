import math

# In các số lẻ từ 17 đến 111 theo thứ tự giảm dần
print("Các số lẻ từ 17 đến 111 (giảm dần):")
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# In các số nguyên tố từ 17 đến 111
print("Các số nguyên tố từ 17 đến 111:")
for i in range(17, 112):
    if is_prime(i):
        print(i, end=" ")
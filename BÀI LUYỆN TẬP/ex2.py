import math

# Nhập hai số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Lũy thừa
power = a ** b

# Căn bậc 2
sqrt_a = math.sqrt(a)
sqrt_b = math.sqrt(b)

# Chia lấy phần nguyên
div_int = a // b

# Chia lấy phần dư
remainder = a % b

# Làm tròn số
round_a = round(a)
round_b = round(b)

# In kết quả
print("Lũy thừa a^b =", power)
print("Căn bậc 2 của a =", sqrt_a)
print("Căn bậc 2 của b =", sqrt_b)
print("Chia lấy phần nguyên a // b =", div_int)
print("Chia lấy phần dư a % b =", remainder)
print("Làm tròn a =", round_a)
print("Làm tròn b =", round_b)
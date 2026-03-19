# Hàm đệ quy tính giai thừa
def factorial(n):
    if n == 0 or n == 1:   # điều kiện dừng
        return 1
    else:
        return n * factorial(n - 1)

# Nhập dữ liệu
n = int(input("Nhập số n: "))

# In kết quả
print("Giai thừa =", factorial(n))
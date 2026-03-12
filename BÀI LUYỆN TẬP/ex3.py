# Nhập số
n = int(input("Nhập một số từ 1 đến 9: "))

# Kiểm tra điều kiện
if 1 <= n <= 9:
    for i in range(1, 10):
        print(n, "x", i, "=", n * i)
else:
    print("Vui lòng nhập số trong khoảng từ 1 đến 9")
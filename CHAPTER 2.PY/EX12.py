#Bài 12
n = int(input("Nhập số nguyên dương n: "))

tong = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        tong += i

print("Tổng các số lẻ từ 1 đến", n, "là:", tong)
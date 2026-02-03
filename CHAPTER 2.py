#Bài 1
n = int(input("Nhập một số từ 1 đến 9: "))

if 1 <= n <= 9:
    print(f"Bảng cửu chương của {n}:")
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")
else:
    print("Vui lòng nhập số trong khoảng từ 1 đến 9.")

#Bài 2
n = int(input("Nhập một số dương: "))

if n <= 1:
    print(n, "không phải là số nguyên tố")
else:
    la_so_nguyen_to = True

    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

#Bài 3
n = int(input("Nhập số n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương")
elif n == 1:
    print(0)
else:
    a = 0
    b = 1
    print(a, b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

#Bài 4
n = int(input("Nhập một số: "))

tong = 0
n = abs(n)   # phòng trường hợp nhập số âm

while n > 0:
    tong = tong + (n % 10)
    n = n // 10

print("Tổng các chữ số là:", tong)

#Bài 5
s = input("Nhập chuỗi: ")
ch = input("Nhập ký tự cần đếm: ")

dem = 0

for ky_tu in s:
    if ky_tu == ch:
        dem += 1

print("Ký tự", ch, "xuất hiện", dem, "lần trong chuỗi")

#Bài 6
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Không tính được giai thừa của số âm")
else:
    print(n, "! =", giaithua(n))

#Bài 7
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

ucln = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i

print("Ước số chung lớn nhất của", a, "và", b, "là:", ucln)

#Bài 8
n = int(input("Nhập một số dương: "))

dao = 0

while n > 0:
    dao = dao * 10 + (n % 10)
    n = n // 10

print("Số sau khi đảo là:", dao)

#Bài 9
n = int(input("Nhập số nguyên dương 5 chữ số: "))

max_digit = 0

while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n = n // 10

print("Chữ số lớn nhất trong số đã nhập là:", max_digit)

#Bài 10
def tong(n):
    if n == 1:
        return 1
    else:
        return n + tong(n - 1)

n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương")
else:
    print("Tổng từ 1 đến", n, "là:", tong(n))

#Bài 11
diem = float(input("Nhập điểm trung bình: "))

if diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")

#Bài 12
n = int(input("Nhập số nguyên dương n: "))

tong = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        tong += i

print("Tổng các số lẻ từ 1 đến", n, "là:", tong)

#Bài 13
mat_khau = ""

while mat_khau != "python123":
    mat_khau = input("Nhập mật khẩu: ")

print("Mật khẩu đúng. Đăng nhập thành công!")

#Bài 14
n = int(input("Nhập số nguyên dương n: "))

if n <= 1:
    print(n, "không phải là số nguyên tố")
else:
    la_so_nguyen_to = True

    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

#Bài 15
n = int(input("Nhập số nguyên dương: "))

tong = 0

while n > 0:
    tong = tong + (n % 10)
    n = n // 10

print("Tổng các chữ số là:", tong)





















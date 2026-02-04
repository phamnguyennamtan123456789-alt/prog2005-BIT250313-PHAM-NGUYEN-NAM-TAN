#Bài 15
n = int(input("Nhập số nguyên dương: "))

tong = 0

while n > 0:
    tong = tong + (n % 10)
    n = n // 10

print("Tổng các chữ số là:", tong)
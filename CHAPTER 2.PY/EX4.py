#Bài 4
n = int(input("Nhập một số: "))

tong = 0
n = abs(n)   # phòng trường hợp nhập số âm

while n > 0:
    tong = tong + (n % 10)
    n = n // 10

print("Tổng các chữ số là:", tong)
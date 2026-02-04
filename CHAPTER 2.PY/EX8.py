#Bài 8
n = int(input("Nhập một số dương: "))

dao = 0

while n > 0:
    dao = dao * 10 + (n % 10)
    n = n // 10

print("Số sau khi đảo là:", dao)
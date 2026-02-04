#Bài 7
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

ucln = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i

print("Ước số chung lớn nhất của", a, "và", b, "là:", ucl
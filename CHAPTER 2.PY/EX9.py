#Bài 9
n = int(input("Nhập số nguyên dương 5 chữ số: "))

max_digit = 0

while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    n = n // 10

print("Chữ số lớn nhất trong số đã nhập là:", max_digit)

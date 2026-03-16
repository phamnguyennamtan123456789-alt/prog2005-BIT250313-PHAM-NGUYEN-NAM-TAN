s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0
dacbiet = 0
khoangtrang = 0
nguyenam = 0
phuam = 0

for c in s:
    if c.isupper():
        hoa += 1
    elif c.islower():
        thuong += 1

    if c.isdigit():
        so += 1

    if c.isspace():
        khoangtrang += 1

    if not c.isalnum() and not c.isspace():
        dacbiet += 1

    if c.lower() in "aeiou":
        nguyenam += 1

    if c.isalpha() and c.lower() not in "aeiou":
        phuam += 1

print("Số chữ cái in hoa:", hoa)
print("Số chữ cái in thường:", thuong)
print("Số chữ số:", so)
print("Số ký tự đặc biệt:", dacbiet)
print("Số khoảng trắng:", khoangtrang)
print("Số nguyên âm:", nguyenam)
print("Số phụ âm:", phuam)
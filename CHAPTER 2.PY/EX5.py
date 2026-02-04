#Bài 5
s = input("Nhập chuỗi: ")
ch = input("Nhập ký tự cần đếm: ")

dem = 0

for ky_tu in s:
    if ky_tu == ch:
        dem += 1

print("Ký tự", ch, "xuất hiện", dem, "lần trong chuỗi")
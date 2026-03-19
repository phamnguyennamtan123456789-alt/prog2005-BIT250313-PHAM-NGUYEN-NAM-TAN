# Nhập dữ liệu
s = input("Nhập chuỗi: ")
k = input("Nhập ký tự cần đếm: ")

count = 0

# Duyệt từng ký tự trong chuỗi
for i in s:
    if i == k:
        count += 1

# In kết quả
print("Số lần xuất hiện:", count)
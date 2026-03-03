# Nhập danh sách số từ người dùng
nhap = input("Nhập các số nguyên cách nhau bởi dấu cách: ")
ds = list(map(int, nhap.split()))

print("Các số lẻ trong danh sách là:")

# Duyệt và in các số lẻ
for so in ds:
    if so % 2 != 0:
        print(so)
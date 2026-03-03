# Nhập danh sách số từ người dùng
nhap = input("Nhập các số nguyên cách nhau bởi dấu cách: ")
ds = list(map(int, nhap.split()))

tong_chan = 0

print("Các số chẵn trong danh sách là:")

for so in ds:
    if so % 2 == 0:
        print(so)
        tong_chan += so

print("Tổng các số chẵn là:", tong_chan)
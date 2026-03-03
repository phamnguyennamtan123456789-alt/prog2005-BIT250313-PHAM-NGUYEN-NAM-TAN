# Nhập danh sách số từ người dùng
nhap = input("Nhập các số cách nhau bởi dấu cách: ")
ds = list(map(int, nhap.split()))

# Nhập số cần tìm
x = int(input("Nhập số cần tìm: "))

# Thuật toán tìm kiếm tuyến tính
vi_tri = -1  # giả sử chưa tìm thấy

for i in range(len(ds)):
    if ds[i] == x:
        vi_tri = i
        break  # dừng lại khi tìm thấy

# In kết quả
if vi_tri != -1:
    print("Số", x, "được tìm thấy tại chỉ số:", vi_tri)
else:
    print("Không tìm thấy số", x, "trong danh sách")
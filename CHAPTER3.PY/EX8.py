# Nhập danh sách số từ người dùng
nhap = input("Nhập các số cách nhau bởi dấu cách: ")
ds = list(map(float, nhap.split()))

# Tìm số đầu tiên lớn hơn 10
so_tim_duoc = None

for so in ds:
    if so > 10:
        so_tim_duoc = so
        break  # dừng ngay khi tìm thấy

# In kết quả
if so_tim_duoc is not None:
    print("Số đầu tiên lớn hơn 10 là:", so_tim_duoc)
else:
    print("Không có số nào lớn hơn 10 trong danh sách")
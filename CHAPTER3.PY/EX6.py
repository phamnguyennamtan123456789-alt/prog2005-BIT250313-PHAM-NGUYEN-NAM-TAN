# Nhập danh sách số nguyên từ người dùng
nhap = input("Nhập các số nguyên cách nhau bởi dấu cách: ")

# Chuyển sang danh sách số nguyên
ds = list(map(int, nhap.split()))

# Biến đếm số lần hoán đổi
so_lan_hoan_doi = 0

# Thuật toán Bubble Sort (tăng dần)
n = len(ds)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ds[j] > ds[j + 1]:
            # Hoán đổi
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
            so_lan_hoan_doi += 1

# In kết quả
print("Danh sách sau khi sắp xếp tăng dần:")
print(ds)
print("Số lần hoán đổi là:", so_lan_hoan_doi)
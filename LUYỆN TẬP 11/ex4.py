ds = [1, 3, 5, 7]

# Thêm phần tử
x = int(input("Nhập số cần thêm: "))
ds.append(x)

# Kiểm tra số lần xuất hiện
k = int(input("Nhập giá trị k: "))
print("Số lần xuất hiện:", ds.count(k))

# Hàm kiểm tra số nguyên tố
def la_nt(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tính tổng số nguyên tố
tong = 0
for x in ds:
    if la_nt(x):
        tong += x

print("Tổng số nguyên tố:", tong)

# Sắp xếp
ds.sort()
print("Danh sách sau sắp xếp:", ds)

# Xóa danh sách
ds.clear()
print("Danh sách sau khi xóa:", ds)
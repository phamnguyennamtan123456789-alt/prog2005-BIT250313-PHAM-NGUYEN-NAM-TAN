# Tạo danh sách 6 số nguyên
ds_so = [8, 5, 3, 5, 10, 1]

print("Danh sách ban đầu:", ds_so)

# Sắp xếp tăng dần
ds_so.sort()
print("Danh sách sau khi sắp xếp tăng dần:", ds_so)

# Đảo ngược danh sách
ds_so.reverse()
print("Danh sách sau khi đảo ngược:", ds_so)

# Đếm số lần xuất hiện của số 5
dem = ds_so.count(5)
print("Số 5 xuất hiện", dem, "lần trong danh sách")
# Nhập danh sách số thực từ người dùng
nhap = input("Nhập các số thực cách nhau bởi dấu cách: ")

# Chuyển chuỗi thành danh sách số thực
ds = list(map(float, nhap.split()))

# Thuật toán Insertion Sort (sắp xếp giảm dần)
for i in range(1, len(ds)):
    key = ds[i]
    j = i - 1

    # So sánh để sắp xếp giảm dần
    while j >= 0 and ds[j] < key:
        ds[j + 1] = ds[j]
        j -= 1

    ds[j + 1] = key

# In kết quả
print("Danh sách sau khi sắp xếp giảm dần:")
print(ds)
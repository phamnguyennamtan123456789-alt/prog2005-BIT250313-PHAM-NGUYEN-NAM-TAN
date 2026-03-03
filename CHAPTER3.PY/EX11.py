# Nhập danh sách số từ người dùng
nhap = input("Nhập các số cách nhau bởi dấu cách: ")
ds = list(map(float, nhap.split()))

# Giả sử phần tử đầu tiên là lớn nhất và nhỏ nhất
max_value = ds[0]
min_value = ds[0]

# Duyệt các phần tử còn lại
for so in ds:
    if so > max_value:
        max_value = so
    if so < min_value:
        min_value = so

# In kết quả
print("Giá trị lớn nhất là:", max_value)
print("Giá trị nhỏ nhất là:", min_value)
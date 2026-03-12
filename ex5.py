import random

# Nhập kích thước ma trận
m = int(input("Nhập số hàng (M): "))
n = int(input("Nhập số cột (N): "))

# Tạo ma trận ngẫu nhiên
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1, 100))
    matrix.append(row)

# Hiển thị ma trận
print("Ma trận:")
for row in matrix:
    print(row)

# Hiển thị hàng theo yêu cầu
r = int(input("Nhập số hàng cần hiển thị: "))
print("Hàng", r, ":", matrix[r-1])

# Hiển thị cột theo yêu cầu
c = int(input("Nhập số cột cần hiển thị: "))
print("Cột", c, ":")
for i in range(m):
    print(matrix[i][c-1])

# Tìm giá trị lớn nhất
max_value = matrix[0][0]
for row in matrix:
    for value in row:
        if value > max_value:
            max_value = value

print("Giá trị lớn nhất trong ma trận:", max_value)
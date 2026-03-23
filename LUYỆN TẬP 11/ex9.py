r = int(input("Nhập số dòng: "))
c = int(input("Nhập số cột: "))

A = []
B = []

print("Nhập ma trận A:")
for i in range(r):
    row = list(map(int, input().split()))
    if len(row) != c:
        print("Lỗi nhập!")
        exit()
    A.append(row)

print("Nhập ma trận B:")
for i in range(r):
    row = list(map(int, input().split()))
    if len(row) != c:
        print("Lỗi nhập!")
        exit()
    B.append(row)

# Cộng ma trận
C = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Ma trận tổng:")
for row in C:
    print(row)
# Nhập số hàng và số cột
m = int(input("Nhập số hàng (m): "))
n = int(input("Nhập số cột (n): "))

print("Nhập ma trận thứ nhất:")
A = []
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    A.append(hang)

print("Nhập ma trận thứ hai:")
B = []
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    B.append(hang)

# Tạo ma trận kết quả
C = []

for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    C.append(hang)

# In ma trận kết quả
print("Ma trận sau khi cộng là:")
for hang in C:
    print(hang)
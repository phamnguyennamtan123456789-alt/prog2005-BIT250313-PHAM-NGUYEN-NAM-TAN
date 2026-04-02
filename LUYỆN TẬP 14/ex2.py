n = int(input("Nhap n: "))

# Hình 1
print("Hinh 1:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Hình 2
print("\nHinh 2:")
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

# Hình 3
print("\nHinh 3:")
for i in range(n):
    for j in range(n):
        if j >= n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 4
print("\nHinh 4:")
for i in range(n):
    for j in range(n):
        if i >= j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 5
print("\nHinh 5:")
for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 6 (hình vuông rỗng)
print("\nHinh 6:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("  *", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 7 (chữ L ngược)
print("\nHinh 7:")
for i in range(n):
    for j in range(n):
        if i == n-1 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 8 (kim tự tháp rỗng)
print("\nHinh 8:")
for i in range(n):
    for j in range(2*n):
        if j == n-i-1 or j == n+i-1 or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Hình 9 (tam giác lệch phải)
print("\nHinh 9:")
for i in range(n):
    for j in range(n):
        if j == n-i-1 or i == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 10 (dấu X)
print("\nHinh 10:")
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
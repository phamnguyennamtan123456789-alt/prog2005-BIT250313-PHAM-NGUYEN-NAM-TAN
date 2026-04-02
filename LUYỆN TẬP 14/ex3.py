n = int(input("Nhap n: "))

# Hình 1
print("Hinh 1:")
for i in range(n):
    for j in range(n):
        print("1", end=" ")
    print()

# Hình 2
print("\nHinh 2:")
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()

# Hình 3
print("\nHinh 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Hình 4
print("\nHinh 4:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Hình 5
print("\nHinh 5:")
for i in range(1, n+1):
    print("  "*(i-1), end="")
    for j in range(1, n-i+2):
        print(j, end=" ")
    print()

# Hình 6
print("\nHinh 6:")
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1:
            print(j, end=" ")
        elif j == 1:
            print(1, end=" ")
        elif j == n - i + 2:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 7
print("\nHinh 7:")
for i in range(1, n+1):
    print("  "*(n-i), end="")
    if i == 1:
        print("1")
    elif i == n:
        for j in range(1, n+1):
            print(j, end=" ")
        print()
    else:
        print(i, " "*(2*i-3), i)

# Hình 8
print("\nHinh 8:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

# Hình 9
print("\nHinh 9:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
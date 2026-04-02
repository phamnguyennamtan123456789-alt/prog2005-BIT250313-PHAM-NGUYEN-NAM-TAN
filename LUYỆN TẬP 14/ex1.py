# Nhập dữ liệu từ bàn phím
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Vòng lặp ngoài quản lý số hàng
for i in range(m):
    # Vòng lặp trong quản lý số cột
    for j in range(n):
        print("*", end="  ")
    # Sau khi in hết một hàng thì xuống dòng
    print()
tong = 0
print("Các số chẵn từ 1 đến 20 là:")

for i in range(2, 21, 2):
    print(i, end=" ")
    tong += i

print(f"\nTổng của các số chẵn này là: {tong}")
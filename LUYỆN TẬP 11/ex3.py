lst = list(map(int, input("Nhập danh sách số: ").split()))

tong = 0

print("Các số chẵn là:")
for x in lst:
    if x % 2 == 0:
        print(x, end=" ")
        tong += x

print("\nTổng số chẵn:", tong)
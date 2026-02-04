#Bài 14
n = int(input("Nhập số nguyên dương n: "))

if n <= 1:
    print(n, "không phải là số nguyên tố")
else:
    la_so_nguyen_to = True

    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
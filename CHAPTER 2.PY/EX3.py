#Bài 3
n = int(input("Nhập số n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương")
elif n == 1:
    print(0)
else:
    a = 0
    b = 1
    print(a, b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
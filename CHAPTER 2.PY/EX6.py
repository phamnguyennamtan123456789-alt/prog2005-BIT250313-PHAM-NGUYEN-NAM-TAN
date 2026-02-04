#Bài 6
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)

n = int(input("Nhập số nguyên không âm: "))

if n < 0:
    print("Không tính được giai thừa của số âm")
else:
    print(n, "! =", giaithua(n))

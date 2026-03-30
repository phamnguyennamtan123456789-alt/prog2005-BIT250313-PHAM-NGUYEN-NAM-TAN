def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

so = int(input("Nhập số cần tính giai thừa: "))
if so < 0:
    print("Vui lòng nhập số không âm.")
else:
    print(f"{so}! = {giai_thua(so)}")
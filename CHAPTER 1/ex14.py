import math

num = float(input("Nhập một số: "))
if num >= 0:
    print("Căn bậc hai là:", math.sqrt(num))
else:
    print("Lỗi: Không thể tính căn bậc hai của số âm.")
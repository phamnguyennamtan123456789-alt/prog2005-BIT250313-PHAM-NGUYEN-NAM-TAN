import math

n = float(input("Nhập một số: "))

if n < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm.")
else:
    ket_qua = math.sqrt(n)
    print(f"Căn bậc hai của {n} là: {ket_qua}")
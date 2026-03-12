# Nhập điểm sinh viên
diem = float(input("Nhập điểm sinh viên: "))

# Kiểm tra điểm hợp lệ
if 0 <= diem <= 10:
    print("Điểm hợp lệ:", diem)
else:
    print("Điểm không hợp lệ! Điểm phải nằm trong khoảng 0 đến 10.")
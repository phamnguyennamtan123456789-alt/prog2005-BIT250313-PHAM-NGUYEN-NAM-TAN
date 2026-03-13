# Hàm tính điểm trung bình
def tinh_diem_trung_binh(ds):
    tong = 0
    so_sv = len(ds)

    for diem in ds.values():
        tong = tong + diem

    trung_binh = tong / so_sv
    return trung_binh


# Chương trình chính
sinh_vien = {}

n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm: "))
    sinh_vien[ten] = diem

tb = tinh_diem_trung_binh(sinh_vien)

print("Danh sách sinh viên:", sinh_vien)
print("Điểm trung bình:", tb)
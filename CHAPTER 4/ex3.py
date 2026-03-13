# Tạo dictionary
sinh_vien = {
    "An": 8,
    "Bình": 7,
    "Chi": 9
}

# Nhập key cần kiểm tra
ten = input("Nhập tên sinh viên cần kiểm tra: ")

# Kiểm tra key
if ten in sinh_vien:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại trong dictionary")
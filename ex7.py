class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

# Khởi tạo 2 đối tượng sinh viên
sv1 = Student("An", 8.5)
sv2 = Student("Bình", 7.8)

# In thông tin
print("Sinh viên 1:", sv1.ten, "-", sv1.diem)
print("Sinh viên 2:", sv2.ten, "-", sv2.diem)
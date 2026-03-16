class SinhVien:
    count = 0   # biến class để đếm số đối tượng

    def __init__(self, name):
        self.name = name
        SinhVien.count += 1   # mỗi lần tạo đối tượng thì tăng lên

    @classmethod
    def dem_so_sinh_vien(cls):
        return cls.count


# Tạo các đối tượng
sv1 = SinhVien("Nam")
sv2 = SinhVien("Lan")
sv3 = SinhVien("Huy")

# In số lượng sinh viên đã tạo
print("Số sinh viên đã tạo:", SinhVien.dem_so_sinh_vien())
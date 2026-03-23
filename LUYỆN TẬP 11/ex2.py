def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Nếu tìm thấy chuỗi tại vị trí mid
        if arr[mid] == target:
            return mid

        # Nếu chuỗi cần tìm đứng sau chuỗi tại mid theo bảng chữ cái
        elif arr[mid] < target:
            left = mid + 1

        # Nếu chuỗi cần tìm đứng trước chuỗi tại mid
        else:
            right = mid - 1

    return -1


# 1. Giả sử đây là danh sách 5 chuỗi đã sắp xếp từ bài trước
danh_sach = ["Anh", "Binh", "Chien", "Dung", "Hoa"]

# 2. Nhập chuỗi từ bàn phím
print(f"Danh sach hien tai: {danh_sach}")
x = input("Nhap chuoi bat ky can tim kiem: ")

# 3. Goi ham tim kiem
vi_tri = binary_search(danh_sach, x)

# 4. In ket qua
if vi_tri != -1:
    print(f"Ket qua: Tim thay '{x}' tai vi tri index {vi_tri}")
else:
    print(f"Ket qua: Khong tim thay chuoi '{x}' trong danh sach.")
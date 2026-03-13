def thong_ke_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat


# Ví dụ sử dụng
t = (3, 7, 1, 9, 4)

tong, lon, nho = thong_ke_tuple(t)

print("Tổng:", tong)
print("Lớn nhất:", lon)
print("Nhỏ nhất:", nho)
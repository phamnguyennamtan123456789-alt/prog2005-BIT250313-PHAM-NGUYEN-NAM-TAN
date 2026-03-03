# Nhập chuỗi từ người dùng
chuoi = input("Nhập một chuỗi: ")

# Chuẩn hóa chuỗi (viết thường để so sánh)
chuoi = chuoi.lower()

# Kiểm tra Palindrome
if chuoi == chuoi[::-1]:
    print("Đây là chuỗi đối xứng (Palindrome)")
else:
    print("Đây không phải là chuỗi đối xứng")
# Tạo danh sách chứa 5 màu sắc
mau_sac = ["Red", "Blue", "Green", "Yellow", "Black"]

print("Danh sách ban đầu:", mau_sac)

# Dùng remove() và xử lý lỗi nếu không tồn tại
try:
    mau_sac.remove("Green")
    print("Đã xóa màu Green khỏi danh sách.")
except ValueError:
    print("Không tìm thấy màu Green trong danh sách.")

# In danh sách sau khi thực hiện
print("Danh sách sau khi xử lý:", mau_sac)
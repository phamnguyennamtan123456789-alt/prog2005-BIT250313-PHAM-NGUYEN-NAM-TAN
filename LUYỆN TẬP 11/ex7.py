import csv

ten = input("Tên: ")
tuoi = input("Tuổi: ")
id_nv = input("ID: ")

# Ghi file text
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"{ten} - {tuoi} - {id_nv}")

# Ghi file csv
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([ten, tuoi, id_nv])

print("Đã lưu file. Hãy mở file để chụp ảnh.")
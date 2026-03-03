# Nhập chuỗi
chuoi = input("Nhập một chuỗi: ")

dao_nguoc = ""

# Duyệt từ cuối về đầu
for i in range(len(chuoi) - 1, -1, -1):
    dao_nguoc += chuoi[i]

print("Chuỗi sau khi đảo ngược là:", dao_nguoc)
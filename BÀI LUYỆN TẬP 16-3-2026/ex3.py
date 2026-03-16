name = input("Nhập tên: ")

name = name.strip()       #bỏ khoảng trắng đầu và cuối
words = name.split()      #tách các từ

result = ""
for w in words:
    result += w.capitalize() + " "

result = result.strip()    #bỏ khoảng trắng cuối
print ("Tên sau khi chuẩn hóa:", result )
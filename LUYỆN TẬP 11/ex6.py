n = int(input("Nhập số người: "))
d = {}

for i in range(n):
    ten = input("Tên: ")
    tuoi = int(input("Tuổi: "))
    d[ten] = tuoi

# Tính tuổi trung bình
tb = sum(d.values()) / len(d)
print("Tuổi trung bình:", tb)

# Selection sort giảm dần theo tuổi
items = list(d.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i + 1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

print("Sau khi sắp xếp:")
for ten, tuoi in items:
    print(ten, tuoi)
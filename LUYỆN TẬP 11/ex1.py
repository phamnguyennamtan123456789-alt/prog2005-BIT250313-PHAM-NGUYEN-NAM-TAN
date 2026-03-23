# Nhập 5 chuỗi
ds = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    ds.append(s)

# Insertion sort theo độ dài giảm dần
for i in range(1, len(ds)):
    key = ds[i]
    j = i - 1

    while j >= 0 and len(ds[j]) < len(key):
        ds[j + 1] = ds[j]
        j -= 1

    ds[j + 1] = key

    print(f"Bước {i}: {ds}")

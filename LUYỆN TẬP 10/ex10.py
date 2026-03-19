arr = []

# Nhập 5 chuỗi
for i in range(5):
    s = input(f"Nhập chuỗi {i+1}: ")
    arr.append(s)

n = len(arr)

# Bubble sort
for i in range(n):
    for j in range(0, n - i - 1):
        if len(arr[j]) < len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print("Bước:", arr)

print("Kết quả:", arr)
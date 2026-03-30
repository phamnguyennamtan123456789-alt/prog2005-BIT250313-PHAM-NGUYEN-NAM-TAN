def bubble_sort(arr):
    n = len(arr)
    # Duyệt qua tất cả các phần tử trong dãy
    for i in range(n):
        # Những phần tử cuối cùng đã được sắp xếp đúng chỗ
        for j in range(0, n - i - 1):
            # Nếu phần tử hiện tại lớn hơn phần tử kế tiếp thì hoán đổi
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ví dụ sử dụng
day_so = [64, 34, 25, 12, 22, 11, 90]
print("Dãy trước khi sắp xếp:", day_so)
bubble_sort(day_so)
print("Dãy sau khi sắp xếp: ", day_so)
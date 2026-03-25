try:
    num1 = int(input("Nhập số bị chia: "))
    num2 = int(input("Nhập số chia: "))
    result = num1 / num2
    print("Kết quả:", result)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0!")
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập số nguyên!")
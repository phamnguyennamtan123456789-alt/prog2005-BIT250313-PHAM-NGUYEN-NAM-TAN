while True:
    print("\n===== MENU =====")
    print("1. Bài 4")
    print("2. Bài 6")
    print("3. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        s = input("Nhập chuỗi: ")
        if s == "":
            print("Lỗi chuỗi rỗng")
        else:
            print(len(s))

    elif choice == "2":
        s = input("Nhập chuỗi: ")
        reverse = ""
        for i in s:
            reverse = i + reverse
        print(reverse)

    elif choice == "3":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")
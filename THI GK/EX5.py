def bai1():
    print("Bạn đã chọn Bài 1")

def bai2():
    print("Bạn đã chọn Bài 2")

def bai3():
    print("Bạn đã chọn Bài 3")

def bai4():
    print("Bạn đã chọn Bài 4")

while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("0. Thoát")

    choice = input("Chọn chương trình: ")

    if choice == "1":
        bai1()
    elif choice == "2":
        bai2()
    elif choice == "3":
        bai3()
    elif choice == "4":
        bai4()
    elif choice == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
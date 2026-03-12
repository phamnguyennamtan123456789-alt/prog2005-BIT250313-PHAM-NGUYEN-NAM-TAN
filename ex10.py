# Hàm thêm sản phẩm vào file
def add_product():
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))

    with open("products.txt", "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")

# Hàm đọc và hiển thị sản phẩm
def display_products():
    print("\nDanh sách sản phẩm:")
    with open("products.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# Hàm sắp xếp theo giá giảm dần
def sort_products():
    products = []

    with open("products.txt", "r", encoding="utf-8") as f:
        for line in f:
            code, name, price = line.strip().split(";")
            products.append([code, name, float(price)])

    products.sort(key=lambda x: x[2], reverse=True)

    print("\nSản phẩm sau khi sắp xếp theo giá giảm dần:")
    for p in products:
        print(f"{p[0]};{p[1]};{p[2]}")

# Chương trình chính
add_product()
display_products()
sort_products()
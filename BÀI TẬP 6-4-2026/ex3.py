class Book:
    # Constructor (Hàm khởi tạo)
    def __init__(self, name, price):
        self.__name = name    # Thuộc tính private (dấu __)
        self.__price = price

    # Getter cho thuộc tính name
    def get_name(self):
        return self.__name

    # Getter cho thuộc tính price
    def get_price(self):
        return self.__price

    # Setter cho thuộc tính name
    def set_name(self, name):
        self.__name = name

    # Setter cho thuộc tính price
    def set_price(self, price):
        self.__price = price

# Khởi tạo 1 đối tượng Book
my_book = Book("Lập trình Python", 120000)

# In ra giá trị price của đối tượng
print(f"Giá của cuốn sách là: {my_book.get_price()}")
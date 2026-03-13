class Product:
    def __init__(self, price):
        self._price = 0
        self.set_price(price)

    # Getter
    def get_price(self):
        return self._price

    # Setter (kiểm tra giá > 0)
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải lớn hơn 0")

    # Hàm in thông tin
    def __str__(self):
        return f"Price của product là: {self._price}"


# Tạo đối tượng
p1 = Product(100)

# In thông tin
print(p1)
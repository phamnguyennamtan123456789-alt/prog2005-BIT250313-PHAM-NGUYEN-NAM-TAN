class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# Tạo đối tượng từ chuỗi
p = Person.from_string("Nam-20")

# In thông tin
print(p)
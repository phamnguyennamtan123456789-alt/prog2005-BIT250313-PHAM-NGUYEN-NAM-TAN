class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   # gọi constructor của lớp cha

    def sound(self):
        print("Gâu gâu")   # ghi đè phương thức sound


# Tạo đối tượng Dog
d = Dog("Milo")

print("Tên:", d.name)
d.sound()
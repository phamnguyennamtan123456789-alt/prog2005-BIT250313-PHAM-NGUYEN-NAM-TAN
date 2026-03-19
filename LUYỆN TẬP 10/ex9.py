class Person:
    count = 0   # class variable

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Person.count += 1

    # getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # setter + validate (cách 1)
    def set_name(self, name):
        if name == "":
            raise ValueError("Tên không được rỗng")
        self._name = name

    # setter + validate (cách 2)
    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._age = age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"

    # phương thức đối tượng
    def greet(self):
        print("Hello,", self._name)

    # class method
    @classmethod
    def get_count(cls):
        return cls.count

    # static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # nạp chồng ==
    def __eq__(self, other):
        return self._age == other._age


# Class kế thừa
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def __str__(self):
        return super().__str__() + f", Score: {self.score}"


# Test
p1 = Person("An", 20)
p2 = Person("Bình", 20)
s1 = Student("Cường", 19, 8.5)

print(p1)
p1.greet()

print("So sánh:", p1 == p2)

print("Tổng đối tượng:", Person.get_count())
print("Có phải người lớn:", Person.is_adult(20))

print(s1)
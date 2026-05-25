class Person:
    @staticmethod
    def add(a, b):
        return a + b
    gender = "male"
    @classmethod
    def gender_info(cls):
        print(cls.gender)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def person_info(self):
        return f"{self.name} is {self.age} years old."
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person1.gender_info()
print(Person.add(5, 3))
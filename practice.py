
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height:float = height
obj1 = Person("Alice", 5)
print(obj1.height)
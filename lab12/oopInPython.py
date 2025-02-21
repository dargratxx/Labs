# classes and objects
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)  # 5

# using __init__ to set up an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name, p1.age)  # John 36

# customizing __str__ so printing the object looks nice
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
print(p1)  # John(36)

# adding a method to a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print(f"hello, my name is {self.name}")
p1.myfunc()

# modifying and deleting attributes on the fly
p1.age = 40
print(p1.age)  # 40
del p1.age  # deleting an attribute

# an empty class just to have it
class EmptyClass:
    pass

# inheritance basics
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print(f"welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")
x = Student("Mike", "Olsen", 2019)
x.welcome()

# polymorphism in action
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("sail!")
class Plane(Vehicle):
    def move(self):
        print("fly!")
vehicles = [Car("Ford", "Mustang"), Boat("Ibiza", "Touring 20"), Plane("Boeing", "747")]
for v in vehicles:
    print(v.brand, v.model)
    v.move()

class Person:
    # init method or constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def intro(self):
        print(f'Hello, my name is {self.__name}.\n\tI am {self.__age} years old.\n')

r = Person('Ahmed', 43)
r.intro()


# Build a rectangle class and sove for area and perimeter
# i.e class Rectangle:
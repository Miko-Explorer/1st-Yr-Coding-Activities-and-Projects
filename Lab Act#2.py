#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area_r = 0
        self.area_c = 0
        self.area_t = 0
        self.base = 0
        self.height = 0
        self.length = 0
        self.width = 0
        self.radius = 0

    @abstractmethod
    def calculateArea(self):
        pass

    def display_circle(self):
        print("Area of a circle:", self.area_c)

    def display_rectangle(self):
        print("Area of a rectangle:", self.area_r)

    def display_triangle(self):
        print("Area of a triangle:", self.area_t)

class AreaCircle(Shape):
    def input_radius(self):
        self.radius = int(input("Enter radius:"))

    def calculateArea(self):
        self.area_c = 3.14 * (self.radius**2)
        return self.area_c

class AreaRectangle(Shape):
    def input_length_width(self):
        self.length = int(input("Enter length:"))
        self.width = int(input("Enter width:"))

    def calculateArea(self):
        self.area_r = self.length * self.width
        return self.area_r

class AreaTriangle(Shape):
    def input_base_height(self):
        self.base = int(input("Enter base:"))
        self.height = int(input("Enter height:"))

    def calculateArea(self):
        self.area_t = 1/2 * (self.base * self.height)
        return self.area_t


AC = AreaCircle()
AR = AreaRectangle()
AT = AreaTriangle()

AC.input_radius()
AC.calculateArea()
AC.display_circle()

print(" ")
AR.input_length_width()
AR.calculateArea()
AR.display_rectangle()

print(" ")
AT.input_base_height()
AT.calculateArea()
AT.display_triangle()

print(" ")

#Encapsulation
class Shape():
    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z

    def AreaTriangle(self):
        triangle = self.x * (self._y * self.__z)
        return "Area of triangle", triangle

    def get_z(self):
        return self.__z

    def set_z(self, z):
        if z > 0:
            self.__z = z
        else:
            print("Invalid input")

SH = Shape(1/2, 90, 100)

print(SH.AreaTriangle())
print("Default value:", SH.x)
print("Width:", SH._y)
print("Original value:", SH.get_z())
print("\t")

SH.set_z(90)
print(SH.AreaTriangle())

SH._y = 60
print(SH.AreaTriangle())

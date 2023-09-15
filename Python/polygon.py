import math

length = 10
width = 5

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return self.length * 4


rectangle = Rectangle(length, width)
rectanglearea = rectangle.area()
rectangleperimeter = rectangle.perimeter()
print("The area of the rectangle is: ", rectanglearea)
print("The perimeter of the rectangle is: ", rectangleperimeter)


square = Square(length)
squarearea = square.area()
squareperimeter = square.perimeter()
print("The area of the square is: ", squarearea)
print("The perimeter of the square is: ", squareperimeter)

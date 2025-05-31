#Class Rectangle with area and perimeter

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(5, 3)
print(f"Area of rectangle: {rectangle.area()}")  
print(f"Perimeter of rectangle: {rectangle.perimeter()}")  

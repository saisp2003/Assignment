#Abstract base class with abc

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

circle = Circle()
print(f"Circle area: {circle.area()}")  

    
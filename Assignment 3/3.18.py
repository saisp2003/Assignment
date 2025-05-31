#Constructor overloading with default arguments

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
point1 = Point() 
point2 = Point(5, 10)  
point1.display()  
point2.display()  
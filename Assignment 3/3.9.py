#Demonstrate single inheritance in Python.

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Example usage
dog = Dog()
dog.sound()  
dog.bark()   

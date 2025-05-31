#Add a method to the `Person` class that prints a greeting

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example usage:
person = Person("Anil", 20) 
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.


#Demonstrate use of `isinstance()` with a class

class Animal:
    pass

dog = Animal()
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object)) 

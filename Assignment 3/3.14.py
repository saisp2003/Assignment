#Demonstrate multiple inheritance in Python.
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")

pet = Pet()
pet.sound()  
pet.bark()   
pet.meow()  
pet.play()   
print("Demonstrating multiple inheritance:")
print("Pet can do the following:")
print("1. Make an animal sound")
print("2. Bark like a dog")
print("3. Meow like a cat")
print("4. Play as a pet")
print("Demonstration complete.")

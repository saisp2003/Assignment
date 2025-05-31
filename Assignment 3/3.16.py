#Polymorphism with a common method

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
    animal.speak()

animal_sound(Cat())
animal_sound(Dog())

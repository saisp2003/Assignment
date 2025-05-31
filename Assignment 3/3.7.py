#Use a method to set attributes

class Car:
    def set_details(self, brand, model):
        self.brand = brand
        self.model = model


car = Car()
car.set_details("Toyota", "Corolla")
print(f"Car brand: {car.brand}, Model: {car.model}")  
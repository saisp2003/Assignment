#Class with class and instance variables

class Example:
    class_var = "I am a class variable"

    def __init__(self, instance_var):
        self.instance_var = instance_var
    def display(self):
        print(f"Class Variable: {Example.class_var}")
        print(f"Instance Variable: {self.instance_var}")

example = Example("I am an instance variable")
example.display()








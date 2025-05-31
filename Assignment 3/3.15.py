#Encapsulation with getter and setter

class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value


student = Student()
student.set_marks(85)
print(f"Student marks: {student.get_marks()}")  

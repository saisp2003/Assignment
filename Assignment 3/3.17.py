#Track number of Employee objects

class Employee:
    count = 0

    def __init__(self):
        Employee.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total employees: {cls.count}")


employee1 = Employee()
employee2 = Employee()
Employee.show_count() 
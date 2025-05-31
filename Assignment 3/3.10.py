#Multilevel inheritance

class A:
    def show_a(self):
        print("This is class A")

class B(A):
    def show_b(self):
        print("This is class B")

class C(B):
    def show_c(self):
        print("This is class C")


c = C()
c.show_a()  
c.show_b()  
c.show_c()  

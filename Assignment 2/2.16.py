#Create a function that accepts a number and prints its multiplication table

def multiply_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
n = int(input("Enter a number: "))
multiply_table(n)

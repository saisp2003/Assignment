#Recursive factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
example_number = 5
result = factorial(example_number)

print(f"The factorial of {example_number} is {result}")
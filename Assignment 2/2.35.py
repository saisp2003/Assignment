#Return product of variable number of arguments

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result


result = multiply_all(2, 3, 4)
print(f"The product of the numbers is: {result}")

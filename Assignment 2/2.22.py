#Find LCM of two numbers


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = 12
num2 = 15
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")
                    





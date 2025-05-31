#Check if a number is an Armstrong number

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

example_number = 153
result = is_armstrong(example_number)
print(f"{example_number} is an Armstrong number: {result}")
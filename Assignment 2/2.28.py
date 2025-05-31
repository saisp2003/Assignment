#Compute power using recursion

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


base = 2
exp = 3
result = power(base, exp)
print(f"{base} raised to the power of {exp} is {result}")
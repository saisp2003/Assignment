#Sum of digits of a number

num = 123
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)

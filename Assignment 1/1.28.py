#Sum of even numbers in a list

lst = [1, 2, 3, 4, 5, 6]
total = 0
for num in lst:
    if num % 2 == 0:
        total += num
print("Sum of even numbers:", total)

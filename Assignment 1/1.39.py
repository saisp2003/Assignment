#Count uppercase and lowercase letters

s = "Hello World"
upper = lower = 0
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

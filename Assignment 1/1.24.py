#Count vowels in a string

s = "Hello World"
count = 0
for char in s:
    if char.lower() in "aeiou":
        count += 1
print("Vowel count:", count)

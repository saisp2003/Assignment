#Check if a number is a palindrome

num = 121
original = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Palindrome" if rev == original else "Not Palindrome")

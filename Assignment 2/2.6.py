#write a function to check if a string is palindrome

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print(is_palindrome("Anna"))




#create a function to count number of vowels in a string
def count_vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("hello world"))


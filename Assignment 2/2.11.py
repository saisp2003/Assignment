#Create a function to count how many times a character appears in a string
def count_char(s, char):
    count = 0
    for i in s:
        if i == char:
            count += 1
    return count
print(count_char("Hello World", "d"))



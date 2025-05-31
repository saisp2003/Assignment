#Check if all characters in a string are unique

def all_unique_characters(s):
    return len(set(s)) == len(s)


print(all_unique_characters("hello"))  
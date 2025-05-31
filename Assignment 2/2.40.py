#Count uppercase and lowercase characters

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count


example_string = "Hello World!"
upper_count, lower_count = count_case(example_string)
print(f"In the string '{example_string}', there are {upper_count} uppercase and {lower_count} lowercase characters.")

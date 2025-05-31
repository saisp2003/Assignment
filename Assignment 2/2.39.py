#Create a function that accepts a list and a value, and returns the index of the value (or -1) without using try.

def find_index(lst, value):
    if value in lst:
        return lst.index(value)
    else:
        return -1

# Example usage 
example_list = [10, 20, 30, 40, 50]
value_to_find = 30
index = find_index(example_list, value_to_find)
print(f"The index of {value_to_find} in {example_list} is {index}")

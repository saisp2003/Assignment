#Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

example_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(example_list)
print(result)

#Return list of (element, index) tuples

def element_index_pairs(lst):
    return list(enumerate(lst))

example_list = ['apple', 'banana', 'cherry']
result = element_index_pairs(example_list)
print(f"List of (element, index) pairs: {result}")

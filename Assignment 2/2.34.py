#Find intersection of two lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

example_list1 = [1, 2, 3, 4, 5]
example_list2 = [4, 5, 6, 7, 8]
result = intersection(example_list1, example_list2)
print(f"The intersection of {example_list1} and {example_list2} is {result}")
#Check if a list is sorted

def is_sorted(lst):
    return lst == sorted(lst)

example_list = [1, 2, 3, 4, 5]
result = is_sorted(example_list)
print(f"Is the list {example_list} sorted? {result}")
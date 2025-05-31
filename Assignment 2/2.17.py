#Write a function that accepts a list and returns the list in reverse order.

def reverse_list(lst):
    return lst[::-1]


example_list = [1, 2, 3, 4, 5]
result = reverse_list(example_list)
print(result)  
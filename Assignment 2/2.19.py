#Create a function that accepts a list of integers and returns only the even ones.
def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(example_list)  
print(result)  
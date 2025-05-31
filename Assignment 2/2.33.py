#Return median of a list

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

example_list = [3, 1, 4, 2, 5]
result = median(example_list)
print(f"The median of {example_list} is {result}")

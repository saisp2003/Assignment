#Flatten a nested list

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested_list = [1, [2, 3], [4, [5, 6]], 7]
flattened_list = flatten(nested_list)
print(f"Flattened list: {flattened_list}")

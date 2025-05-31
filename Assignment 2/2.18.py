#Write a function to find the second largest number in a list.
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None

Example_list = [10, 20, 4, 45, 99]
result = second_largest(Example_list)
print(result) 
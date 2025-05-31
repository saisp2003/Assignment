#write a function that returns the average of a list of numbers

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]
result = average(numbers)
print(result)  
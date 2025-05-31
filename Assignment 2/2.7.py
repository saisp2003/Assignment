#check a function to calculate the sum of a list of numbers
def sum_of_list(num):
    total = 0
    for i in num:
        total += i
    return total
print(sum_of_list([10, 20, 30, 40, 50]))


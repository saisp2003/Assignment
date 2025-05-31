#Write a function to find the minimum value in a list
def min_value(num):
    min_value = num[0]
    for i in num:
        if i < min_value:
            min_value = i
    return min_value    
print(min([10, 20, 30, 40, 50]))


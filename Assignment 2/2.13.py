#Create a function to find the sum of digits of a number

def sum_of_digits(n):
    total=0
    while n>0:
        total +=n%10
        n //= 10
    return total
print(sum_of_digits(12345))  

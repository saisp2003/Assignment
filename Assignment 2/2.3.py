#create a function to find the maximum of three numbers
def max_number(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print(max_number(10, 20, 30))

        

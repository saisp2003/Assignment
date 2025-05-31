#Count frequency of digits in a number

num = 1122339087
num_str = str(num)
digit_count = {}
for digit in num_str:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1
print("Digit frequency:", digit_count)

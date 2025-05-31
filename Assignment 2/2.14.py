#Write a function that takes a string and returns a dictionary of  character frequencies

def char_frequencies(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


text = "hello world"
result = char_frequencies(text)
print(result)




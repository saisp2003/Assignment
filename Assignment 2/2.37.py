#Word count in a string

def word_count(s):
    words = s.split()
    return len(words)


sentence = "The quick brown fox jumps over the lazy dog"
result = word_count(sentence)
print(f"The number of words in the sentence is: {result}") 
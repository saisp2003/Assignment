#Return the longest word in a sentence

def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

sentence = "The quick brown fox jumps over the lazy dog"
result = longest_word(sentence)
print(f"The longest word in the sentence is: '{result}'")

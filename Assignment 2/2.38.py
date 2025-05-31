# Check if a sentence is a pangram

def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return alphabet.issubset(sentence_set)

sentence = "The quick brown fox jumps over the lazy dog"
result = is_pangram(sentence)
print(f"Is the sentence a pangram? {result}")  
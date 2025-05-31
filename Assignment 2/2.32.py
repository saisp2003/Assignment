#Find most frequent element

from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

example_list = [1, 2, 3, 2, 4, 2, 5]
result = most_frequent(example_list)
print(f"The most frequent element in {example_list} is {result}")

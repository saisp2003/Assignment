#Two independent objects

class Counter:
    def __init__(self):
        self.count = 0

a = Counter()
b = Counter()
a.count += 1
print(a.count)  
print(b.count)  

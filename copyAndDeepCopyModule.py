import copy
spam = ['A', 'B', 'C', 'D']
id(spam)
print(id(spam))
cheese = copy.copy(spam)
id(cheese)
print(id(cheese))
cheese[1] = 42
print(spam)
print(cheese)
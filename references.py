spam = [0, 1, 2, 3, 4, 5]
print(spam)
cheese = spam # The reference is being copied, not the list.
print(cheese)
cheese[1] = 'Hello!' # This changes the list value.
print(spam)
print(cheese)
spam = ['Ant', 'Turtle', 'Bee', 'Whale', 'Cat', 'Dog', 'Moose']
spam.insert(1, 'Chicken') # This will insert 'Chicken' into the list at index 1
spam.sort(reverse=True) # This will sort the list in reverse
print(spam)

# sort() uses ASCIIbetical order, therefore the lowercase letters are before the uppercase letters
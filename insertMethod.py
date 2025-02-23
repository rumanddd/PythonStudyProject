spam = ['Ant', 'Turtle', 'Bee', 'Whale', 'Cat', 'Dog', 'Moose']
spam.insert(1, 'Chicken') # This will insert 'Chicken' into the list at index 1
spam.sort(reverse=True) # This will sort the list in reverse
print(spam)

# sort() uses ASCIIbetical order, therefore the lowercase letters are before the uppercase letters
# If you need to sort the values in regular alphabetical order, pass str.lower for the key keyword argument in the sort() method call.
    # This causes the sort() function to treat all the items in the list as if they were lowercase without actually changing the values in the list.
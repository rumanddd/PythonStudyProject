# The tuple data type is almost identical to the list data type, except in two ways:
# 1. Tuples are defined using parentheses ( ) instead of square brackets [ ].
# 2. Tuples are immutable, meaning they cannot be modified after creation.

# Creating a tuple
my_tuple = ('apple', 24, 0.2)  # A tuple containing a string, an integer, and a float
print(my_tuple)  # Prints ('apple', 24, 0.2)

# Single-value tuples must have a trailing comma; otherwise, Python treats them as regular values.
print(type(('hello',)))  # Correct: This is a tuple
print(type(('hello')))  # Incorrect: This is a string, not a tuple

# Converting data types using list() and tuple() functions
print(tuple(['Cat', 'Dog', 5]))  # Converts a list to a tuple: ('Cat', 'Dog', 5)
print(list(('Cat', 'Dog', 5, 2)))  # Converts a tuple to a list: ['Cat', 'Dog', 5, 2]
print(list('Hello'))  # Converts a string to a list: ['H', 'e', 'l', 'l', 'o']

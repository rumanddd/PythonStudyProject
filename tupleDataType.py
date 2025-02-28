# The tuple data type is almost identical to the list data type, except in two ways.
# First, tuples are typed with parentheses, ( and ), instead of square brackets, [ and ].
# Second, tuples are immutable, which means they cannot be changed once they are created.

# Creating a tuple
my_tuple = ('apple', 24, 0.2)
print(my_tuple)

# If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses.
# Otherwise, Python will think you’ve just typed a value inside regular parentheses.
# The comma is what lets Python know this is a tuple value.

type(('hello',)) # This is a tuple
type(('hello')) # This is a string

# Converting Types with the list() and tuple() Functions
print(tuple(['Cat', 'Dog', 5])) # This will convert a list to a tuple, ('Cat', 'Dog', 5)
print(list(('Cat', 'Dog', 5, 2))) # This will convert a tuple to a list, ['Cat', 'Dog', 5]
print(list('Hello')) # This will convert a string to a list, ['H', 'e', 'l', 'l', 'o']
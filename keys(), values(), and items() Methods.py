# Define a dictionary named 'spam' with two key-value pairs
spam = {'color': 'red', 'age': '24'}

# Iterate over the values in the dictionary using .values()
# .values() returns only the values ('red', '24') of the dictionary
for v in spam.values():
    # Print each value
    print(v)

# Note: If we change spam.values() to spam.keys(), the loop will iterate over the keys
# ('color', 'age') instead of the values, so the output would be:
# color
# age
# spam.items() is a method that returns a list of tuples (key, value)
name = 'Robot'  # Assign a name
age = 101  # Assign an age

# Check conditions in sequence
if name == 'Alice':
    print('Hi, Alice.')  # If the name is "Alice", print this
elif age < 12:
    print('You are not Alice, kiddo.')  # If age is below 12, print this
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')  # If age is unrealistic, print this
elif age > 100:
    print('You are not Alice, grannie.')  # If over 100, print this (this runs for age = 101)
elif age > 12:
    print('You are not Alice, middle aged person.')  # If greater than 12 but <=100, print this

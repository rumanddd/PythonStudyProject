# Initialize the variable `name` to an empty string
name = ''

# Ask for the user's name
while not name:
    print('Enter your name:')
    name = input()  # Keeps asking until a valid name is entered

# Ask how many guests the user will have
print('How many guests will you have?')
# Convert user input to an integer
numofGuests = int(input())

# Check if numofGuests is greater than 0
if numofGuests:
        print('Be sure to have enough room for all your guests.')

print('Done')

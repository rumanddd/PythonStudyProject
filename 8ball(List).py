import random  # Importing the random module for generating random numbers

# Creating a list of possible messages
messages = [
    'It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful'
]

# Generating a random index between 0 and the last index of the messages list
random_index = random.randint(0, len(messages) - 1)

# Printing a random message using the generated index
print(messages[random_index])

'''
Explanation:
- `random.randint(0, len(messages) - 1)` generates a random number within the valid index range of the list.
- The random index is then used to retrieve a message from the `messages` list.
- This simulates an "8-ball" style random response generator.
'''

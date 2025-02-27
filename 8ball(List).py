import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

''' Prints a random message from the list of messages using the random module and the random.randint()
function to generate a random number between 0 and the length of the messages list minus 1 (0-indexed).
The resulting index is then used to access the corresponding message in the messages list. '''
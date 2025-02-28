import random  # Import the random module

# Generate a random number (either 1, 2, or 3) and store it in 'spam'
spam = random.randint(1, 3)

# Check the value of 'spam' and print the corresponding message
if spam == 1:
    print('Hello')  # Print "Hello" if spam is 1
elif spam == 2:
    print('Howdy')  # Print "Howdy" if spam is 2
else:
    print('Greetings!')  # Print "Greetings!" if spam is anything else (in this case, 3)

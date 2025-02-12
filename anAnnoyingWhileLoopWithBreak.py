# Start an infinite loop
while True:
    # Prompt the user to type their name
    print('Please type your name.')
    # Read the user's input and store it in the variable 'name'
    name = input()
    # Check if the entered name is exactly 'your name'
    if name == 'your name':
        # If the condition is met, exit the loop
        break
# This line executes after the loop has been exited
print('Thank you!')

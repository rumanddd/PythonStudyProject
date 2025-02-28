while True:  # Infinite loop to keep asking for input
    print('Who are you?')
    name = input()  # Ask for the name

    if name != 'Joe':
        continue  # If name is not "Joe", restart the loop

    print('Hello, Joe! What is the password? (It is a fish.)')
    password = input()  # Ask for the password

    if password == 'swordfish':
        break  # If password is correct, exit the loop

print('Access granted.')  # Print success message after exiting loop

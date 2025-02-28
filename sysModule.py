import sys  # Import the sys module to use sys.exit()

while True:  # Infinite loop
    print('Type exit to exit')  # Prompt the user to type "exit"
    response = input()  # Take user input

    if response == 'exit':
        sys.exit()  # If user types "exit", terminate the program

    # This line runs only if the user didn't type "exit"
    print('You typed ' + response)

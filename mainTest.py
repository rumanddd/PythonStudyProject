# This program says hello and asks for my name.
print("Hello, There!")
print("What is your name?")  # Asks for your name.

myName = input()  # Store the name once

# If the name is "Ruman", ask for a password
if myName == "Ruman":
    password = input("Enter password: ")  # Ask for the password
    if password == "ruru":  # Check if the password is correct
        print("Access granted.")
    elif password == "1234": # Handles a SPECIFIC wrong password with a message
        print("WRONG! That's the kind of password everyone uses on their suitcase, dummy.")
        exit()  # End the program immediately
    # For elif statements the order matters

    else:
        print("Access denied.")  # Incorrect password
        exit()  # End the program immediately
else:
    print('You do not have access to the rest of this code.')
    exit()  # End the program immediately if the name is incorrect

# If the name and password are correct, the rest of the code runs
print("It's nice to meet you, " + myName)
print("The length of your name is: " + str(len(myName)) + " characters long")  # Combined into one print

print("What is your age?")  # Asks for your age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

print('I have eaten ' + str(99) + ' burritos.')

# Examples of comparison operators in action:
x = 10  # Example value for x
y = 20  # Example value for y

print(x == y)  # Equal to (False)
print(x != y)  # Not equal to (True)
print(x > y)  # Greater than (False)
print(x < y)  # Less than (True)
print(x >= y)  # Greater than or equal to (False)
print(x <= y)  # Less than or equal to (True)

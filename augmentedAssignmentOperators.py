# Assigning an integer value to the variable 'spam'
spam = 42  # 'spam' is initialized with the value 42
print(spam)  # Prints 42

# A while loop that runs as long as 'spam' is less than 50
while spam < 50:
    if spam == 42:  # If 'spam' is exactly 42
        spam += 1  # Increment 'spam' by 1
        continue  # Skip the rest of the loop body and start the next iteration

    print(spam)  # Prints the current value of 'spam' (if not skipped by 'continue')
    spam += 1  # Increments 'spam' by 1 (same as spam = spam + 1)
    print(spam)  # Prints the updated value of 'spam'

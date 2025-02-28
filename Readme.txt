# Python Study Project # 

This repository contains various Python scripts and notes to help reinforce programming concepts. It serves as a personal reference guide, documenting key ideas, syntax rules, and useful tips.

## Key Learnings & Notes

### Loops

You can only use continue and break statements inside while and for loops.

A while loop can accomplish the same tasks as a for loop, though for loops are often more concise.

### Functions & Arguments

Some functions, like range(), accept multiple arguments separated by commas.

Example: range(start, stop, step) allows control over the sequence of numbers.

Functions can have default parameter values and accept keyword arguments.

### List & Tuple Operations

Lists are mutable, meaning they can be modified after creation, whereas tuples are immutable.

Useful list methods:

.append(value) → Adds a value to the end of a list.

.insert(index, value) → Inserts a value at a specified index.

.copy() vs. copy.deepcopy() → The latter is used for deep copying nested lists.

Tuples support tuple unpacking, allowing values to be extracted into separate variables:

coordinates = (10, 20)
x, y = coordinates  # x = 10, y = 20

### Modules & Imports

The random module allows random selection from lists using random.choice().

import sys enables program termination via sys.exit().

### Miscellaneous Tips

The id() function returns an object’s memory address.

The in and not in operators check for membership in sequences (lists, strings, tuples, etc.).

Global and local variables can have the same name, but local variables take precedence within functions.

## File Overview

This repository contains multiple Python scripts, each demonstrating different concepts:

RockPaperScissors.py → A simple game implementing user input and conditional statements.

guessTheNumberGame.py → A number guessing game utilizing loops and random module.

theCollatzSequence.py → Implements the famous Collatz sequence.

stringMutation.py → Demonstrates immutability of strings.

tupleUnpacking.py → Shows how tuple unpacking works.

## How to Use

Clone the repository:

git clone https://github.com/rumanddd/PythonStudyProject.git

Navigate to the folder:

cd PythonStudyProject

Run a script:

python script_name.py

(Replace script_name.py with the actual script filename.)

## Contributing

This repository is mainly for personal learning, but if you'd like to contribute or discuss ideas, feel free to open an issue!

## License

This project is for educational purposes and is free to use.


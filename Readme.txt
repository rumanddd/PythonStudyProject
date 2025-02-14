This readme file is just little notes for me to remember some important things I've learned:


- You can only use continue and break statements inside while and for loops.

- You can actually use a while loop to do the same thing as a for loop; for loops are just more concise.

- Some functions can be called with multiple arguments separated by a comma, and range() is one of them.
   This lets you change the integer passed to range() to follow any sequence of integers, including starting at a number other than zero.
# for i in range(12, 16):
    print(i)
- The first argument will be where the for loop’s variable starts, and the second argument will be up to, but not including, the number to stop at.


- The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.
# for i in range(0, 10, 2):
    print(i)
- So calling range(0, 10, 2) will count from zero to eight by intervals of two.


- You can also use the range() function to count backwards.
# for i in range(10, -1, -1):
    print(i)

***Importing Modules***

- Python has built-in functions like print(), input(), and len(). It also includes a standard library with modules like math for mathematical functions and random for randomness.
   To use a module, you must first import it with an import statement.
- DO NOT give them a name python file names a same name that is used by one of Python’s modules.
- Here’s an example of an import statement that imports four different modules:
    import random, sys, os, math
- You can also import all functions from a module with a from statement.
    for example, from random import *

- Parameters are like empty boxes waiting for values.
- Arguments are the values you put inside those boxes when calling the function.
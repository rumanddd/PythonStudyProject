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

-The call stack is a technical detail that you don’t strictly need to know about to write programs.
    It’s enough to understand that function calls return to the line number they were called from.
    However, understanding call stacks makes it easier to understand local and global scopes

- Scopes matter for several reasons:
   * Code in the global scope, outside of all functions, cannot use any local variables.
   * However, code in a local scope can access global variables.
   * Code in a function’s local scope cannot use variables in any other local scope.
   * You can use the same name for different variables if they are in different scopes.
     That is, there can be a local variable named spam and a global variable also named spam.

- So far from my understand a global scope is a variable that is defined outside of any function.
- A local scope is a variable that is defined inside a function (Indented)

- There are four rules to tell whether a variable is in a local scope or global scope:
   * If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.
   * If there is a global statement for that variable in a function, it is a global variable.
   * Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
   * But if the variable is not used in an assignment statement, it is a global variable.

If you ever want to modify the value stored in a global variable from IN a function, you must use a global statement on that variable.

- A method is the same thing as a function, except it is “called on” a value.
- A function is a block of code that performs a task. A method is a block of code that performs a task on a value.
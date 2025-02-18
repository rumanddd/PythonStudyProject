# Define function a()
def a():
    print('a() starts')  # Indicate the start of function a
    b()  # Call function b
    d()  # Call function d
    print('a() returns')  # Indicate the end of function a

# Define function b()
def b():
    print('b() starts')  # Indicate the start of function b
    c()  # Call function c
    print('b() returns')  # Indicate the end of function b

# Define function c()
def c():
    print('c() starts')  # Indicate the start of function c
    print('c() returns')  # Indicate the end of function c

# Define function d()
def d():
    print('d() starts')  # Indicate the start of function d
    print('d() returns')  # Indicate the end of function d

# Call function a() to start execution
a()

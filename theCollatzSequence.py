def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result

n = int(input("Give me a number: "))
steps = 0  # Counter to track the number of steps

while n != 1:
    n = collatz(n)
    steps += 1  # Increment counter

print(f"It took {steps} steps to reach 1.")

# For even numbers divide by 2, for odd numbers multiply by 4 and add 1
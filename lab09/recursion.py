# recursion.py

# Task 1: Recursive function to calculate the product of the digits of an integer
def product_of_digits(x):
    x = abs(x)  # Ignore the minus sign if x is negative
    if x < 10:  # Base case: single-digit number
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)  # Recursive case

# Task 2: Recursive function to convert an array of integers to a comma-separated string
def array_to_string(a, index=0):
    if index >= len(a):  # Base case: if index is out of range
        return ""
    elif index == len(a) - 1:  # Last element, no trailing comma
        return str(a[index])
    else:
        return str(a[index]) + "," + array_to_string(a, index + 1)  # Recursive case

# Task 3: Recursive function to calculate the floor of the logarithm
def log(base, value):
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1.")
    if value < base:  # Base case: quotient is less than the base
        return 0
    else:
        return 1 + log(base, value // base)  # Recursive case

# Testing product_of_digits
print(product_of_digits(234))  # Output should be 24
print(product_of_digits(-12))  # Output should be 2

# Testing array_to_string
print(array_to_string([1, 2, 3, 4]))  # Output should be "1,2,3,4"
print(array_to_string([5]))          # Output should be "5"

# Testing log
print(log(10, 123456))  # Output should be 5
print(log(2, 64))       # Output should be 6
print(log(10, 4567))    # Output should be 3

import math

# Step 1: Input the first side of the triangle
side_a_str = input("Enter the length of the first side (a): ")

# Step 2: Input the second side of the triangle
side_b_str = input("Enter the length of the second side (b): ")

# Step 3: Convert the string inputs to float numbers
side_a = float(side_a_str)
side_b = float(side_b_str)

# Step 4: Calculate the hypotenuse using the Pythagorean theorem
hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)

print(f"The hypotenuse is {hypotenuse:.2f}")

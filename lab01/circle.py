import math

def main():
    # Input the radius of the circle
    radius_input = input("Enter the radius of the circle: ")

    # Convert the input to a numeric variable
    radius = float(radius_input)

    # Compute the area and perimeter of the circle
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius

    # Print the results
    print(f"The circle with radius {radius:.2f} has an area of {area:.2f} and a perimeter of {perimeter:.2f}")

if __name__ == "__main__":
    main()

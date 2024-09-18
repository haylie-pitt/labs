def convert_units(value, unit):
    # Conversion factors
    cm_to_inch = 2.54
    yd_to_m = 0.9144
    oz_to_g = 28.349523125
    lb_to_kg = 0.45359237

    # Convert based on the unit
    if unit == 'in':
        converted_value = value * cm_to_inch
        converted_unit = 'cm'
    elif unit == 'cm':
        converted_value = value / cm_to_inch
        converted_unit = 'in'
    elif unit == 'yd':
        converted_value = value * yd_to_m
        converted_unit = 'm'
    elif unit == 'm':
        converted_value = value / yd_to_m
        converted_unit = 'yd'
    elif unit == 'oz':
        converted_value = value * oz_to_g
        converted_unit = 'g'
    elif unit == 'g':
        converted_value = value / oz_to_g
        converted_unit = 'oz'
    elif unit == 'kg':
        converted_value = value / lb_to_kg
        converted_unit = 'lb'
    elif unit == 'lb':
        converted_value = value * lb_to_kg
        converted_unit = 'kg'
    else:
        return "Invalid unit"

    # Return the converted value and unit
    return round(converted_value, 2), converted_unit

def main():
    # Ask user for input
    user_input = input("Enter value and unit (e.g., '19.342124 cm'): ").strip()
    try:
        # Split input into value and unit
        value_str, unit = user_input.split()
        value = float(value_str)

        # Convert units
        converted_value, converted_unit = convert_units(value, unit)

        # Display result
        if isinstance(converted_value, str):  # If invalid unit
            print(converted_value)
        else:
            print(f"{value:.2f} {unit} = {converted_value:.2f} {converted_unit}")

    except ValueError:
        print("Invalid input format. Please use '<value> <unit>' format.")

if __name__ == "__main__":
    main()

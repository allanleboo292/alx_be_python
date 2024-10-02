FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction starts here
try:
    # Prompt user for temperature input
    temp_input = input("Enter the temperature to convert: ")
    temperature = float(temp_input)  # Attempt to convert input to a float

    # Prompt user for the temperature unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # Convert from Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {converted_temp:.2f}°C")
    elif unit == 'C':
        # Convert from Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {converted_temp:.2f}°F")
    else:
        # Invalid unit entered
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    # Handle non-numeric temperature input
    print("Invalid temperature. Please enter a numeric value.")


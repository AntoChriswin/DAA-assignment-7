def convert_temperature(celsius):
    kelvin = round(celsius + 273.15, 5)
    fahrenheit = round(celsius * 1.80 + 32.00, 5)
    return [kelvin, fahrenheit]

# Test the function with examples
print(convert_temperature(36.50))  # Output: [309.65000, 97.70000]
print(convert_temperature(122.11))  # Output: [395.26000, 251.79800]

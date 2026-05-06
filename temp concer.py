# Temperature Converter (Corrected Version)

# Celsius to Fahrenheit
cel = float(input("Enter temperature in Celsius: "))
f = (cel * 1.8) + 32
print("Temperature in Fahrenheit:", round(f, 2))

# Fahrenheit to Celsius
f = float(input("\nEnter temperature in Fahrenheit: "))
cel = (f - 32) / 1.8
print("Temperature in Celsius:", round(cel, 2))

# Kelvin to Fahrenheit
k = float(input("\nEnter temperature in Kelvin: "))
f = (k - 273.15) * 1.8 + 32
print("Temperature in Fahrenheit:", round(f, 2))

# Fahrenheit to Kelvin
f = float(input("\nEnter temperature in Fahrenheit: "))
k = (f - 32) / 1.8 + 273.15
print("Temperature in Kelvin:", round(k, 2))

# Kelvin to Celsius
k = float(input("\nEnter temperature in Kelvin: "))
cel = k - 273.15
print("Temperature in Celsius:", round(cel, 2))

# Celsius to Kelvin
cel = float(input("\nEnter temperature in Celsius: "))
k = cel + 273.15
print("Temperature in Kelvin:", round(k, 2))
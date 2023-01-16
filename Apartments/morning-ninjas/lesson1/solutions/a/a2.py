# Write a program that receives a temperature in celsius and prints the temperature in fahrenheit.
# Hint: the formula for the conversion is:
# °F = °C * (9/5) + 32
# For example, the formula that converts 0 °C to fahrenheit is:
# (0°C × 9/5) + 32 = 32°F

temp_c = float(input("Insert temperature in Celsius: "))
temp_f = temp_c * (9/5) + 32
print(f"{temp_c}°C = {temp_f}°F")
def celsius_to_fahrenheit(temperature):
    fahrenheit_temperature = (temperature * 1.8) + 32
    return fahrenheit_temperature


def fahrenheit_to_celsius(temperature):
    celsius_temperature = (temperature - 32) * 0.5556
    return celsius_temperature


print("Enter two temperatures: one in Celsius, second in Fahrenheit")
temperature_in_celsius, temperature_in_fahrenheit = float(input()), float(input())

print(temperature_in_celsius, "°C is", celsius_to_fahrenheit(temperature_in_celsius),"°F")
print(temperature_in_fahrenheit, "°F is", fahrenheit_to_celsius(temperature_in_fahrenheit), "°C")
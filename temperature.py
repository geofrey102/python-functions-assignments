def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Enter temperature in Celsius: "))

result = convert_temperature(celsius)

print("Temperature in Fahrenheit:", format(result, ".2f"))

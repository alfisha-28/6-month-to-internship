temp = float(input("Enter temperature: "))
unit = input("Is this Celsius or Fahrenheit? (C/F): ").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is {fahrenheit:.2f}°F")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is {celsius:.2f}°C")
else:
    print("Invalid unit!")

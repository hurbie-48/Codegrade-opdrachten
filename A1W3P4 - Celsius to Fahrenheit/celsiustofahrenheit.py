def celciusToFahrenheit(celcius:int) -> int:
    fahrenheit = int((celcius * 9/5) + 32)
    return fahrenheit

print("°C °F")
for i in range(1,11):
    print(f"{i*10} {celciusToFahrenheit(i*10)}")


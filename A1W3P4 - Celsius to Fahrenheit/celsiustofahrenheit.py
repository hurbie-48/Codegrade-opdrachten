def celsius_to_fahrenheit(celsius: int) -> int:
    fahrenheit = int((celsius * 9/5) + 32)
    return fahrenheit


print("°C °F")
for i in range(1, 11):
    temp_c = i * 10
    print(f"{temp_c} {celsius_to_fahrenheit(temp_c)}")
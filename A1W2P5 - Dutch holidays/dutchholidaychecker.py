dutch_holidays = {
    (1, 1): "Nieuwjaarsdag",
    (4, 27): "Koningsdag",
    (5, 4): "Dodenherdenking",
    (5, 5): "Bevrijdingsdag",
    (12, 5): "Sinterklaas",
    (12, 25): "Eerste Kerstdag",
    (12, 26): "Tweede Kerstdag",
    (12, 31): "Oudejaarsavond"
}

user_input = input("Date: ")
month = user_input.split(": ")[1]

if month[1] == ",":
    month = int(month[0])
else:
    month = int(month[:2])

day = int(user_input.split(": ")[2])
try:
    print(dutch_holidays[month, day])
except KeyError:
    print("No holiday found on given input.")

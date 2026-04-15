class Auto:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year

    def __repr__(self):
        return f"De auto heet: {self.name} en komt uit {self.year}."


class Persoon:
    def __init__(self, name: str, cars: list[Auto]):
        self.name = name
        self.age = 18
        self.cars = cars

    def increase_age(self):
        self.age = 20


auto1 = Auto("Fiets",2007)
auto2 = Auto("Driewieler",2003)
speler1 = Persoon("John",[auto1, auto2])

auto1 = Auto("Vliegend tapijt",2067)
auto2 = Auto("Komkommer-mobiel",2114)
speler2 = Persoon("Dick",[auto1, auto2])

spelers = [speler1, speler2]
for speler in spelers:
    print(f"{speler.name} heeft de volgende auto's: ")
    for car in speler.cars:
        print(f"{car}")
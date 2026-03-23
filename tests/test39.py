import random
getallen = []
for i in range(20):
    getallen.append(random.randint(1,100))

print(f"De lijst: {getallen}")
gemiddelde = sum(getallen) / len(getallen)
print(f"Gemiddelde: {gemiddelde}")
print(f"Grootste waarde: {max(getallen)}")
print(f"Kleinste waarde: {min(getallen)}")
gesorteerd = sorted(getallen)
print(f"Tweede kleinste: {gesorteerd[1]}")
print(f"Tweede grootste: {gesorteerd[-2]}")

even_getallen = []
for getal in getallen:
    if getal % 2 == 0:
        even_getallen.append(getal)

print(f"Aantal even getallen: {len(even_getallen)}")
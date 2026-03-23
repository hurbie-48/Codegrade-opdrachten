print("    ", end="")
for label in range(1, 11):
    print(f"{label:4}", end="")
print("\n" + "-" * 45)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    
    for j in range(1, 11):
        product = i * j
        print(f"{product:4}", end="")

    print()
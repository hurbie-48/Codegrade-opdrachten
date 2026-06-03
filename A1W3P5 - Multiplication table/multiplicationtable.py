print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:4}", end="")

    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")

    print()
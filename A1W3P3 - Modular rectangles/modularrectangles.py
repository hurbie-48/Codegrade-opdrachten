width = int(input("Width: "))
height = int(input("Height: "))
count = 0

for h in range(height):
    for w in range(width):
        print(count % 10, end=" ")
        count += 1
    print()
options = [True, False]

print("\n\nAND\n---------")
for A in options:
    for B in options:
        print(f"{A} + {B} = {A and B}")
print("\n")
print("OR\n---------")
for A in options:
    for B in options:
        print(f"{A} + {B} = {A or B}")
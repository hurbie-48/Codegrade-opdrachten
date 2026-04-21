import sys


def tail():
    if len(sys.argv) < 2:
        print("Usage: python3 tail.py <filename>")
        return
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines[-10:]:
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    tail()
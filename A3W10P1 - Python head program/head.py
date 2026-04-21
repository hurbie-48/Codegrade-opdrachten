import sys


def head():
    if len(sys.argv) < 2:
        print("Usage: python3 head.py <filename>")
        return
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            for iteration in range(10):
                line = f.readline()
                if not line:
                    break
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    head()
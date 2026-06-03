import os


def analyze_function_comments():
    user_input = input("Enter python file names (comma separated): ")
    filenames = [name.strip() for name in user_input.split(',')]
    for filename in filenames:
        if not os.path.exists(filename):
            print(f'Error reading file: "{filename}"')
            continue

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                for index, current_line in enumerate(lines):
                    if current_line.startswith('def '):
                        line_number = index + 1
                        has_comment = False

                        if index > 0:
                            previous_line = lines[index - 1]
                            if previous_line.startswith('#'):
                                has_comment = True

                        if not has_comment:
                            raw_name = current_line.split('def ')[1]
                            function_name = raw_name.split('(')[0].strip()

                            print(
                                f"File: {filename} contains a function "
                                f"[{function_name}()] on line [{line_number}] "
                                f"without a preceding comment."
                            )

        except FileNotFoundError:
            print(f'Error reading file: "{filename}"')


if __name__ == "__main__":
    analyze_function_comments()
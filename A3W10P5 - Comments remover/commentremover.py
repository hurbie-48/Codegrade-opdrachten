def remove_python_comments():
    source_path = input("Enter the path of the file to read: ").strip()
    destination_path = input("Enter the path of the file to save: ").strip()

    if source_path == destination_path:
        print("Error: Source and destination files must have different names to prevent data loss.")
        return

    try:
        with open(source_path, 'r', encoding='utf-8') as source_file, \
                open(destination_path, 'w', encoding='utf-8') as clean_file:

            for current_line in source_file:
                left_trimmed = current_line.lstrip()

                if left_trimmed.startswith('#') or not left_trimmed.strip():
                    continue

                if '#' in current_line:
                    current_line = current_line.split('#', 1)[0].rstrip() + '\n'

                clean_file.write(current_line)

        print(f"Success! Cleaned code has been saved to: {destination_path}")

    except FileNotFoundError:
        print(f'Error: Could not find the file located at "{source_path}"')
    except Exception as error_message:
        print(f"An unexpected error occurred while processing: {error_message}")


if __name__ == "__main__":
    remove_python_comments()
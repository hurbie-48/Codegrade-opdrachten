books = []


def print_menu() -> None:
    print("[A] Add book\n[S] Search book\n[E] Exit (and print)")


def validate_input(user_input: str) -> bool:
    user_input.lower()
    if user_input == "a" or user_input == "s" or user_input == "e":
        return True


def add_book(user_input: str) -> None:
    information = [item.strip() for item in user_input.split(",")]
    book_title = information[0]
    book_author = information[1]
    book_publisher = information[2]
    book_pub_date = information[3]
    book = {
        "title": book_title,
        "author": book_author,
        "publisher": book_publisher,
        "pub_date": book_pub_date
    }
    for existing_book in books:
        if existing_book['title'].lower() == book_title.lower():
            print(f"Error: The book '{book_title}' is already in the list.")
            return
    books.append(book)


def search_book(books: list, term: str) -> bool:
    term.lower()
    for book in books:
        if term == book["title"] or term == book["author"] or term == book["publisher"]:
            return True
    return False


def main():
    while True:
        print("\n[A] Add book\n[S] Search book\n[E] Exit (and print)")
        choice = input("Select an option: ").upper()

        if choice == 'A':
            details = input("Book details: ")
            add_book(details)
        elif choice == 'S':
            term = input("Search term: ")
            if search_book(books, term):
                print(f"Found a book for: {term}")
            else:
                print(f"No book found for: {term}")
        elif choice == 'E':
            for book in books:
                print(book)
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
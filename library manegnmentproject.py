def add_book():
    """Add a new book record to the file."""
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Open file in append mode to add a new record
    with open("library.txt", "a") as file:
        file.write(f"{book_id},{title},{author}\n")

    print(f"✅ Book '{title}' added successfully!\n")


def display_books():
    """Display all books from the file."""
    try:
        with open("library.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("📖 No books in the library yet.\n")
                return

            print("\n📚 Library Book Records:")
            print("-" * 40)
            print(f"{'Book ID':<10}{'Title':<15}{'Author'}")
            print("-" * 40)
            for line in lines:
                book_id, title, author = line.strip().split(",")
                print(f"{book_id:<10}{title:<15}{author}")
            print("-" * 40 + "\n")

    except FileNotFoundError:
        print("⚠️ No record found. Add some books first!\n")


def search_book():
    """Search for a book by its title."""
    title_search = input("Enter Book Title to Search: ").strip().lower()
    found = False

    try:
        with open("library.txt", "r") as file:
            for line in file:
                book_id, title, author = line.strip().split(",")
                if title.lower() == title_search:
                    print("\n🔍 Book Found:")
                    print(f"Book ID: {book_id}")
                    print(f"Title: {title}")
                    print(f"Author: {author}\n")
                    found = True
                    break

        if not found:
            print("❌ Book not found!\n")

    except FileNotFoundError:
        print("⚠️ No record found. Add some books first!\n")


def main():
    """Main menu for the Library System."""
    while True:
        print("===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book by Title")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

# Run the program
main()

import json

LIBRARY_FILE = 'library.json'

def load_library():
    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input('Enter the title of your book: ')
    author = input('Enter the name of author: ')
    year = input('Enter the publication year of your book: ')
    genre = input('Enter the genre of your book: ')
    read_status = input('Have you read this book? (y/n): ').strip().lower() == "yes"

    library.append({
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read_status
    })
    print('Book added successfully!')

def remove_book(library):
    title = input("Enter the title of the book you want to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found!")


def book_search(library):
    choice = input("Search by \n1. Title\n2. Author\n Enter your choice: ")
    term = input ("Enter the book title you want to search: ")
    for book in library:
        if choice == "1" and book["title"].lower() == term.lower():
            print(book)
            return
        elif choice == "2" and book["author"].lower() == term.lower():
            print(book)
            return
    print("Book not found!")

def display_all_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("""
         Welcome to your Personal Library Manager!
         1. Add a book
         2. Remove a book
         3. Search for a book
         4. Display all books
         5. Display statistics
         6. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            book_search(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
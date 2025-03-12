import json
from typing import List, TypedDict
import time
import os

# Define TypedDict for book structure
class Book(TypedDict):  
    title: str
    author: str
    year: int
    genre: str
    read: bool
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIBRARY_FILE = os.path.join(BASE_DIR, "library.json")
# Library list containing books

library: List[Book] = []

def load_library() -> List[Book]:
    """Loads the library data from a JSON file."""
    try:
        with open(LIBRARY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file doesn't exist or is corrupted

def save_library(library: List[Book]) -> None:
    """Saves the updated list to JSON, replacing existing data properly."""
    try:
        with open(LIBRARY_FILE, "w", encoding="utf-8") as file:
            json.dump(library, file, indent=4)
            time.sleep(2)
    except Exception as e:
        print(f"❌ Failed to save library to file: {e}")


def add_book(library: List[Book]) -> None:
    """Adds a new book to the library."""
    title = input("📖 Enter the book title: ")
    author = input("✍️ Enter the author: ")
    year = input("📅 Enter the publication year: ")
    genre = input("📚 Enter the genre: ")
    read_status = input("📘 Have you read this book? (yes/no): ").strip().lower() == "yes"

    book: Book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    
    library.append(book)
    save_library(library)  # Save after adding a new book
    print("✅ Book added successfully!\n")

def remove_book(library: List[Book]) -> None:
    """Removes a book by title."""
    title = input("🗑️ Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)# Save after removing a book
            time.sleep(2)
            print("\n✅ Book removed successfully!\n")
            return
    print("❌ Book not found.\n")

def search_book(library: List[Book]) -> None:
    """Searches for a book by title or author."""
    print("🔍 Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        term = input("📖 Enter the title: ").lower()
        results = [book for book in library if term in book["title"].lower()]
    elif choice == "2":
        term = input("✍️ Enter the author: ").lower()
        results = [book for book in library if term in book["author"].lower()]
    else:
        print("❌ Invalid choice.\n")
        return
    
    if results:
        print("📚 Matching Books:")
        for idx, book in enumerate(results, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'📘 Read' if book['read'] else '📕 Unread'}")
    else:
        print("❌ No matching books found.\n")

def display_books(library: List[Book]) -> None:
    """Displays all books in the library."""
    if not library:
        print("📚 No books in the library.\n")
        return
    print("📚 Your Library:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'📘 Read' if book['read'] else '📕 Unread'}")

def display_statistics(library: List[Book]) -> None:
    """Displays total books and read percentage."""
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"📚 Total books: {total_books}")
    print(f"📊 Percentage read: {read_percentage:.2f}%\n")

def main() -> None:
    """Main function to run the library manager."""
    global library
    library = load_library()  # Load books when program starts
    
    while True:
        print(f"\n {"-" *20 }📚 Welcome to your Personal Library Manager!  {"-" *20 } ")
        print("1. ➕ Add a book")
        print("2. 🗑️ Remove a book")
        print("3. 🔍 Search for a book")
        print("4. 📚 Display all books")
        print("5. 📊 Display statistics")
        print("6. 🚪 Exit")
        choice = input("Enter your choice by selecting a Number: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)  # Save before exiting
            print("💾 Library saved to file. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()

# library.py

import json
import os

class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author):
        book = {'title': title, 'author': author}
        self.books.append(book)
        self.save_books()

    def delete_book(self, title):
        self.books = [book for book in self.books if book['title'] != title]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. List Books")
        print("4. Find Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print(f"Book '{title}' by {author} added.")

        elif choice == '2':
            title = input("Enter book title to delete: ")
            library.delete_book(title)
            print(f"Book '{title}' deleted.")

        elif choice == '3':
            books = library.list_books()
            print("\nList of Books:")
            for book in books:
                print(f"Title: {book['title']}, Author: {book['author']}")

        elif choice == '4':
            title = input("Enter book title to find: ")
            book = library.find_book(title)
            if book:
                print(f"Found Book: Title: {book['title']}, Author: {book['author']}")
            else:
                print(f"Book '{title}' not found.")

        elif choice == '5':
            print("Exiting the library management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

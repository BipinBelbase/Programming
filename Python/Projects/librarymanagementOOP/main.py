from library import Library
from book import book
from member import member

# Create a new library instance
libraryxxx = Library()

def display_menu():
    print("\nWelcome to the Library Management System")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display All Books")
    print("4. Display All Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Borrowed Books of a Member")
    print("8. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            title = input("\nEnter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            libraryxxx.add_book(title, author, isbn)
            print(f"\nBook '{title}' added to the library.")

        elif choice == '2':
            name = input("\nEnter member name: ")
            member_id = input("Enter member ID: ")
            libraryxxx.add_member(name, member_id)
            print(f"\nMember '{name}' added to the library.")

        elif choice == '3':
            print("\nBooks in Library:")
            libraryxxx.display_total_books()

        elif choice == '4':
            print("\nLibrary Members:")
            libraryxxx.display_total_members()

        elif choice == '5':
            member_name = input("\nEnter member name to borrow a book: ")
            book_title = input("Enter book title to borrow: ")
            
            # Find member and book
            member_found = None
            book_found = None

            for member in libraryxxx.totalmembers:
                if member.name == member_name:
                    member_found = member
                    break

            for book in libraryxxx.totalbooks:
                if book.title == book_title:
                    book_found = book
                    break

            if member_found and book_found:
                member_found.borrow_book(book_found)
            else:
                print("\nMember or book not found!")

        elif choice == '6':
            member_name = input("\nEnter member name to return a book: ")
            book_title = input("Enter book title to return: ")

            # Find member and book
            member_found = None
            book_found = None

            for member in libraryxxx.totalmembers:
                if member.name == member_name:
                    member_found = member
                    break

            for book in libraryxxx.totalbooks:
                if book.title == book_title:
                    book_found = book
                    break

            if member_found and book_found:
                member_found.return_book(book_found)
            else:
                print("\nMember or book not found!")

        elif choice == '7':
            member_name = input("\nEnter member name to display borrowed books: ")
            libraryxxx.find_borrowed_books(member_name)

        elif choice == '8':
            print("\nExiting the system. Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()

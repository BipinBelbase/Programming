from book import book as bk
from member import member as mem

class Library:
    def __init__(self):
        self.totalbooks = []
        self.totalmembers = []

    def add_book(self, title, author, isbn):
        new_book = bk(title, author, isbn)
        self.totalbooks.append(new_book)

    def add_member(self, name, member_id):
        new_member = mem(name, member_id)
        self.totalmembers.append(new_member)

    def display_total_books(self):
        print("Books in Library:")
        for book in self.totalbooks:
            print(f"{book.title} by {book.author}")

    def display_total_members(self):
        print("Members of the Library:")
        for member in self.totalmembers:
            print(f"{member.name}, ID: {member.member_id}")

    def find_borrowed_books(self, membername):
        for member in self.totalmembers:
            if member.name == membername:
                member.display_info()
                return
        print(f"Member {membername} not found.")


    
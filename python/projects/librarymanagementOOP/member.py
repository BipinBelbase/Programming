class member:
    def __init__(self, name, member_id, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, addbookborrow):
        self.borrowed_books.append(addbookborrow)
        print(f"{self.name} successfully borrowed {addbookborrow.title}")

    def return_book(self, returnbook):
        if returnbook in self.borrowed_books:
            self.borrowed_books.remove(returnbook)
            print(f"{self.name} successfully returned {returnbook.title}")
        else:
            print(f"{self.name} never borrowed the book: {returnbook.title}, recheck please....")

    def display_info(self):
        print(f"***************** {self.name} ***********************")
        print(f"*************** Books You Have Borrowed ***************")
        if not self.borrowed_books:
            print("No books borrowed.")
        for book in self.borrowed_books:
            print(f"--- {book.title} by {book.author}")








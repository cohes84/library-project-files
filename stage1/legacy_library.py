# Legacy system — do not modify
# Written by the previous developer

class Library:
    """Manages everything about the library."""

    def __init__(self, name):
        self.name = name
        self.books = []      # list of dicts
        self.members = []    # list of dicts

    def add_book(self, title, author, isbn):
        for b in self.books:
            if b["isbn"] == isbn:
                print(f"Book {isbn} already exists.")
                return
        self.books.append({
            "title": title, "author": author,
            "isbn": isbn, "available": True
        })
        print(f"Added: {title} by {author}")

    def remove_book(self, isbn):
        for b in self.books:
            if b["isbn"] == isbn:
                self.books.remove(b)
                print(f"Removed book {isbn}")
                return
        print(f"Book {isbn} not found.")

    def search_books(self, query):
        q = query.lower()
        results = [b for b in self.books
                   if q in b["title"].lower()
                   or q in b["author"].lower()]
        if not results:
            print("No books found.")
            return
        for b in results:
            status = "available" if b["available"] else "borrowed"
            print(f"  {b['title']} by {b['author']} [{status}]")

    def get_available_books(self):
        available = [b for b in self.books if b["available"]]
        print(f"\n{self.name} — Available books:")
        for b in available:
            print(f"  {b['title']} by {b['author']}")

    def register_member(self, name, member_id):
        if not member_id.startswith("M") or len(member_id) != 6:
            print(f"Invalid member ID: {member_id}")
            return
        for m in self.members:
            if m["member_id"] == member_id:
                print(f"Member {member_id} already exists.")
                return
        self.members.append({
            "name": name, "member_id": member_id,
            "active_loans": []
        })
        print(f"Registered: {name}")

    def find_member(self, member_id):
        for m in self.members:
            if m["member_id"] == member_id:
                return m
        print(f"Member {member_id} not found.")
        return None

    def checkout(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member:
            return
        book = None
        for b in self.books:
            if b["isbn"] == isbn:
                book = b
                break
        if not book:
            print(f"Book {isbn} not found.")
            return
        if not book["available"]:
            print(f"Book {isbn} is not available.")
            return
        book["available"] = False
        member["active_loans"].append(isbn)
        print(f"{member['name']} checked out {book['title']}")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        if not member or isbn not in member["active_loans"]:
            print("Invalid return.")
            return
        for b in self.books:
            if b["isbn"] == isbn:
                b["available"] = True
                break
        member["active_loans"].remove(isbn)
        print(f"Returned: {isbn}")

    def get_member_loans(self, member_id):
        member = self.find_member(member_id)
        if not member:
            return
        print(f"\nLoans for {member['name']}:")
        for isbn in member["active_loans"]:
            for b in self.books:
                if b["isbn"] == isbn:
                    print(f"  {b['title']}")

    def print_library_status(self):
        print(f"\n{'='*40}")
        print(f"  {self.name}")
        print(f"{'='*40}")
        total = len(self.books)
        available = sum(1 for b in self.books if b["available"])
        borrowed = total - available
        print(f"  Books: {total} total, {available} available, {borrowed} borrowed")
        print(f"  Members: {len(self.members)}")
        print(f"\n  Borrowed books:")
        for b in self.books:
            if not b["available"]:
                for m in self.members:
                    if b["isbn"] in m["active_loans"]:
                        print(f"    {b['title']} -> {m['name']}")
        print(f"{'='*40}\n")
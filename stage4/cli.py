from library import Library


class CLI:
    # Note: all methods here will eventually be redesigned once we cover
    # static methods and other tools. For now we are using a class as a
    # namespace to keep things organised.

    def __init__(self):
        self.lib = Library("City Library")

    def do_add_book(self):
        title  = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn   = input("ISBN: ").strip()
        try:
            self.lib.add_book(title, author, isbn)
            print(f"Added: {title} by {author}")
        except ValueError as e:
            print(f"Error: {e}")

    def do_remove_book(self):
        isbn = input("ISBN: ").strip()
        try:
            self.lib.remove_book(isbn)
            print(f"Removed: {isbn}")
        except KeyError as e:
            print(f"Error: {e}")

    def do_search_books(self):
        query   = input("Search: ").strip()
        results = self.lib.search_books(query)
        if not results:
            print("No books found.")
        for book in results:
            print(f"  {book}")

    def do_available_books(self):
        books = self.lib.get_available_books()
        if not books:
            print("No available books.")
        for book in books:
            print(f"  {book}")

    def do_register_member(self):
        name      = input("Name: ").strip()
        member_id = input("Member ID: ").strip()
        try:
            self.lib.register_member(name, member_id)
            print(f"Registered: {name}")
        except ValueError as e:
            print(f"Error: {e}")

    def do_all_members(self):
        members = self.lib.get_all_members()
        if not members:
            print("No members registered.")
        for member in members:
            print(f"  {member}")

    def do_checkout(self):
        member_id = input("Member ID: ").strip()
        isbn      = input("ISBN: ").strip()
        try:
            self.lib.checkout(member_id, isbn)
            print("Checked out successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def do_return_book(self):
        member_id = input("Member ID: ").strip()
        isbn      = input("ISBN: ").strip()
        try:
            self.lib.return_book(member_id, isbn)
            print("Returned successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def show_menu(self):
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search books")
        print("4. Show available books")
        print("5. Register member")
        print("6. Show all members")
        print("7. Checkout book")
        print("8. Return book")
        print("9. Quit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choice: ").strip()

            if choice == "1":
                self.do_add_book()
            elif choice == "2":
                self.do_remove_book()
            elif choice == "3":
                self.do_search_books()
            elif choice == "4":
                self.do_available_books()
            elif choice == "5":
                self.do_register_member()
            elif choice == "6":
                self.do_all_members()
            elif choice == "7":
                self.do_checkout()
            elif choice == "8":
                self.do_return_book()
            elif choice == "9":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()
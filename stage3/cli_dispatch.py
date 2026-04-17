from library import Library


class CLI:
    # Note: all methods here will eventually be redesigned once we cover
    # static methods and other tools. For now we are using a class as a
    # namespace to keep things organised.

    def __init__(self):
        self.lib = Library("City Library")
        # ── Dispatch table ──────────────────────────────────────────
        # Functions are objects — they can be stored in a dict and
        # called later. self.do_add_book is a method object.
        self.commands = {
            "1": ("Add book",             self.do_add_book),
            "2": ("Remove book",          self.do_remove_book),
            "3": ("Search books",         self.do_search_books),
            "4": ("Show available books", self.do_available_books),
            "5": ("Register member",      self.do_register_member),
            "6": ("Show all members",     self.do_all_members),
            "7": ("Checkout book",        self.do_checkout),
            "8": ("Return book",          self.do_return_book),
        }

    def do_add_book(self):
        title  = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn   = input("ISBN: ").strip()
        self.lib.add_book(title, author, isbn)

    def do_remove_book(self):
        isbn = input("ISBN: ").strip()
        self.lib.remove_book(isbn)

    def do_search_books(self):
        query   = input("Search: ").strip()
        results = self.lib.search_books(query)
        if not results:
            print("No books found.")

    def do_available_books(self):
        self.lib.get_available_books()

    def do_register_member(self):
        name      = input("Name: ").strip()
        member_id = input("Member ID: ").strip()
        self.lib.register_member(name, member_id)

    def do_all_members(self):
        self.lib.get_all_members()

    def do_checkout(self):
        member_id = input("Member ID: ").strip()
        isbn      = input("ISBN: ").strip()
        self.lib.checkout(member_id, isbn)

    def do_return_book(self):
        member_id = input("Member ID: ").strip()
        isbn      = input("ISBN: ").strip()
        self.lib.return_book(member_id, isbn)

    def show_menu(self):
        print("\n--- Library Menu ---")
        for key, (label, _) in self.commands.items():
            print(f"{key}. {label}")
        print("9. Quit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choice: ").strip()

            if choice == "9":
                break
            elif choice in self.commands:
                _, fn = self.commands[choice]
                fn()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()
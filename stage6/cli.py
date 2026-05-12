from library import Library
from employee_manager import EmployeeManager
from employee import Librarian, PartTimeStaff, StudentWorker


class CLI:
    # Note: all methods here will eventually be redesigned once we cover
    # static methods and other tools. For now we are using a class as a
    # namespace to keep things organised.

    def __init__(self):
        self.lib = Library("City Library")
        self.em  = EmployeeManager()

    # ── Library ─────────────────────────────────────────────────────

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
            loan = self.lib.checkout(member_id, isbn)
            print(f"Checked out successfully. Due: {loan.due_date}")
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

    def do_status(self):
        stats = self.lib.get_status()
        loans = self.lib.get_active_loans()
        print(f"\n{'='*40}")
        print(f"  {stats['name']}")
        print(f"{'='*40}")
        print(f"  Books: {stats['total']} total, {stats['available']} available")
        print(f"  Members: {stats['members']}")
        if loans:
            print("\n  Active loans:")
            for title, name in loans:
                print(f"    {title} -> {name}")
        print(f"{'='*40}\n")

    def do_overdue(self):
        loans = self.lib.get_overdue()
        if not loans:
            print("No overdue loans.")
            return
        print("\nOverdue loans:")
        for loan in loans:
            print(f"  {loan}")

    # ── HR ──────────────────────────────────────────────────────────

    def do_add_employee(self):
        print("Type: 1=Librarian  2=PartTimeStaff  3=StudentWorker")
        emp_type  = input("Type: ").strip()
        emp_id    = input("Employee ID: ").strip()
        name      = input("Name: ").strip()
        try:
            if emp_type == "1":
                salary   = float(input("Weekly salary: "))
                employee = Librarian(emp_id, name, salary)
            elif emp_type == "2":
                hours    = float(input("Hours worked: "))
                rate     = float(input("Hour rate: "))
                employee = PartTimeStaff(emp_id, name, hours, rate)
            elif emp_type == "3":
                hours    = float(input("Hours worked: "))
                rate     = float(input("Hour rate: "))
                employee = StudentWorker(emp_id, name, hours, rate)
            else:
                print("Invalid type.")
                return
            self.em.add_employee(employee)
            print(f"Added: {employee}")
        except ValueError as e:
            print(f"Error: {e}")

    def do_all_employees(self):
        employees = self.em.get_all()
        if not employees:
            print("No employees.")
            return
        for emp in employees:
            print(f"  {emp}")

    def do_payroll(self):
        from payroll import PayrollSystem
        PayrollSystem().calculate_payroll(self.em.get_all())

    # ── Menus ────────────────────────────────────────────────────────

    def show_library_menu(self):
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search books")
        print("4. Show available books")
        print("5. Register member")
        print("6. Show all members")
        print("7. Checkout book")
        print("8. Return book")
        print("9. Library status")
        print("10. Show overdue loans")
        print("\n--- HR Menu ---")
        print("11. Add employee")
        print("12. Show all employees")
        print("13. Run payroll")
        print("\n0. Quit")

    def run(self):
        while True:
            self.show_library_menu()
            choice = input("Choice: ").strip()

            if choice == "0":
                break
            elif choice == "1":   self.do_add_book()
            elif choice == "2":   self.do_remove_book()
            elif choice == "3":   self.do_search_books()
            elif choice == "4":   self.do_available_books()
            elif choice == "5":   self.do_register_member()
            elif choice == "6":   self.do_all_members()
            elif choice == "7":   self.do_checkout()
            elif choice == "8":   self.do_return_book()
            elif choice == "9":   self.do_status()
            elif choice == "10":  self.do_overdue()
            elif choice == "11":  self.do_add_employee()
            elif choice == "12":  self.do_all_employees()
            elif choice == "13":  self.do_payroll()
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    cli = CLI()
    cli.run()
from abc import ABC, abstractmethod


class Employee(ABC):
    """Base class for all library employees.

    All subclasses must implement calculate_payroll().
    """

    def __init__(self, employee_id, name):
        """Initialise an employee with an ID and name.

        Args:
            employee_id (str): Unique identifier for the employee.
            name (str): Full name of the employee.
        """
        self.employee_id = employee_id
        self.name        = name

    @abstractmethod
    def calculate_payroll(self):
        """Calculate and return the employee's payroll amount.

        Returns:
            float: The amount to be paid.
        """
        pass

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"


class Librarian(Employee):
    """A salaried librarian employee."""

    def __init__(self, employee_id, name, weekly_salary):
        """Initialise a librarian.

        Args:
            employee_id (str): Unique identifier.
            name (str): Full name.
            weekly_salary (float): Fixed weekly salary.
        """
        super().__init__(employee_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        """Return the fixed weekly salary.

        Returns:
            float: Weekly salary amount.
        """
        return self.weekly_salary


class PartTimeStaff(Employee):
    """An hourly part-time employee."""

    def __init__(self, employee_id, name, hours_worked, hour_rate):
        """Initialise a part-time staff member.

        Args:
            employee_id (str): Unique identifier.
            name (str): Full name.
            hours_worked (float): Number of hours worked this week.
            hour_rate (float): Pay rate per hour.
        """
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hour_rate    = hour_rate

    def calculate_payroll(self):
        """Return hours worked multiplied by the hour rate.

        Returns:
            float: Total pay for hours worked.
        """
        return self.hours_worked * self.hour_rate


class StudentWorker(PartTimeStaff):
    """A student worker — hourly pay capped at MAX_HOURS with a meal allowance."""

    MAX_HOURS      = 20   # class attribute — was global MAX_STUDENT_HOURS
    MEAL_ALLOWANCE = 50   # class attribute — was global MEAL_ALLOWANCE

    def __init__(self, employee_id, name, hours_worked, hour_rate):
        """Initialise a student worker, capping hours at MAX_HOURS.

        Args:
            employee_id (str): Unique identifier.
            name (str): Full name.
            hours_worked (float): Requested hours — capped at MAX_HOURS.
            hour_rate (float): Pay rate per hour.
        """
        actual_hours = min(hours_worked, StudentWorker.MAX_HOURS)
        super().__init__(employee_id, name, actual_hours, hour_rate)

    def calculate_payroll(self):
        """Return base hourly pay plus meal allowance.

        Returns:
            float: Total pay including meal allowance.
        """
        return super().calculate_payroll() + StudentWorker.MEAL_ALLOWANCE

    def __str__(self):
        return super().__str__() + " [student]"
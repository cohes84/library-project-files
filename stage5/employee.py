from __future__ import annotations


class Employee:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name        = name

    def calculate_payroll(self):
        # Every subclass must implement this.
        # Note: Python has a formal mechanism for this called
        # Abstract Base Class (ABC) — we will cover it later.
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement calculate_payroll()"
        )

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id})"


class Librarian(Employee):

    def __init__(self, employee_id, name, weekly_salary):
        super().__init__(employee_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class PartTimeStaff(Employee):

    def __init__(self, employee_id, name, hours_worked, hour_rate):
        super().__init__(employee_id, name)
        self.hours_worked = hours_worked
        self.hour_rate    = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


MAX_STUDENT_HOURS = 20
MEAL_ALLOWANCE    = 50

class StudentWorker(PartTimeStaff):

    def __init__(self, employee_id, name, hours_worked, hour_rate):
        actual_hours = min(hours_worked, MAX_STUDENT_HOURS)
        super().__init__(employee_id, name, actual_hours, hour_rate)

    def calculate_payroll(self):
        return super().calculate_payroll() + MEAL_ALLOWANCE

    def __str__(self):
        return super().__str__() + " [student]"
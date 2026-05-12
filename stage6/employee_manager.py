from employee import Employee

class EmployeeManager:

    def __init__(self):
        self.employees = {}   # employee_id: Employee

    def add_employee(self, employee):
        if employee.employee_id in self.employees:
            raise ValueError(
                f"Employee {employee.employee_id} already exists."
            )
        self.employees[employee.employee_id] = employee

    def get_employee(self, employee_id):
        if employee_id not in self.employees:
            raise KeyError(f"Employee {employee_id} not found.")
        return self.employees[employee_id]

    def get_by_type(self, employee_type):
        return [e for e in self.employees.values()
                if issubclass(type(e), employee_type)]

    def get_all(self):
        return list(self.employees.values())
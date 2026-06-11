class Employee:
    def _init_(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role

    def _str_(self):
        return f"Employee: {self.name} - Role: {self.role}"
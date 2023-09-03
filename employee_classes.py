class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        
    def update_salary(self, new_salary):
        self.salary = new_salary
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nDepartment: {self.department}\nSalary: ${self.salary}"

employees = [
    Employee("John Doe", 101, "HR", 50000),
    Employee("Jane Smith", 102, "IT", 60000),
    Employee("Michael Johnson", 103, "Sales", 55000),
    Employee("Emily Williams", 104, "IT", 62000)
]

def update_department_salary(department, new_salary):
    for e in employees:
        if e.department == department:
            e.update_salary(new_salary)

update_department_salary("IT", 65000)

for emp in employees:
    print(emp.__str__())
    print("-------------")
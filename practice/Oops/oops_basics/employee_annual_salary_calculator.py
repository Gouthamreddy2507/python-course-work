class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_annual_salary(self):
        print(f"Annual salary of {self.name} is {self.base_salary*12}")

emp = Employee("goutham",40000)
emp.calculate_annual_salary()
        
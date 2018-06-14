class Employee(object):
    numOfEmp = 0
    def __init__(self):
        self.type = "Developer"

    def calculate(self):
        # to calculate number of employees
        self.numOfEmp += 1
        print("Number of employee:", self.numOfEmp)

    def display(self, name, sal):
        print("Employee Name:",name)
        print("Salary of the Employee:",sal)
        print("Designation of Employee:",self.type)

    def addEmployee(self, name, sal):
        self.display(name, sal)
        self.calculate()
   # def averagesal(self,avgsal):
      #  self.avgsal=

employee = Employee()
employee.addEmployee('sravya', 1000)
employee.addEmployee('vineeth', 2000)

class Manager(Employee):
    def __init__(self):
        self.type = "Manager"

manager = Manager()
manager.addEmployee('XXX', 5000)
    
import datetime


class Employee:
    increment = 1.05
    numberOfEmployee = 0

    def __init__(self, firstname, lastname, age, salary, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary
        self.email = email
        Employee.numberOfEmployee += 1

    def tellFullName(self):
        return f"{self.firstname} {self.lastname}"

    def raise_salary(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def setIncrement(cls, amount):
        cls.increment = amount

    @classmethod
    def employeeFromString(cls, string):
        first, last, age, salary, email = string.split('-')
        return cls(first, last, age, salary, email)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


employee_1 = Employee('John', 'Doe',
                      25, 50000,
                      'johndoe123@gmail.com',
                      )
employee_2 = Employee('Ron', 'Michel',
                      35, 110000,
                      'ronmichel123@gmail.com',
                      )
employee_3 = Employee('Jonathan', 'Smilga',
                      50, 130000,
                      'jonathansmilga123@gmail.com',
                      )
employee_4 = Employee.employeeFromString("""
Aditya-Singh-15-200000-adityasingh27apr@gmail.com
""")

employee_3.leads = [
    employee_1.tellFullName(),
    employee_2.tellFullName()
]

employee_4.leads = [
    employee_1.tellFullName(),
    employee_2.tellFullName(),
    employee_3.tellFullName(),
]

date = datetime.date(2021, 7, 9)
# print(Employee.isWorkDay(date))

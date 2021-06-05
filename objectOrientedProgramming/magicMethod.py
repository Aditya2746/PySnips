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

    def __repr__(self):
        return f"{self.firstname}-{self.lastname}({self.email})-{self.age}"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __add__(self, other):
        return self.salary + other

    def __len__(self):
        return len(self.tellFullName())

class Developer(Employee):
    increment = 1.10

    def __init__(self, firstname, lastname, age, salary, email, programmingLang):
        self.programmingLang = programmingLang
        Employee.__init__(self, firstname, lastname, age, salary, email)


class Manager(Employee):
    increment = 1.11

    def __init__(self, firstname, lastname, age, salary, email, leads=None):
        if leads is None:
            self.leads = []
        else:
            self.leads = leads
        Employee.__init__(self, firstname, lastname, age, salary, email)

    def add_employee(self, employee):
        if employee not in self.leads:
            self.leads.append(employee)

    def remove_employee(self, employee):
        if employee in self.leads:
            self.leads.remove(employee)

    def allUnder(self):
        return self.leads


employee_1 = Developer('John', 'Doe',
                       25, 50000,
                       'johndoe123@gmail.com',
                       'Java'
                       )
employee_2 = Developer('Ron', 'Michel',
                       35, 110000,
                       'ronmichel123@gmail.com',
                       'Python'
                       )
employee_3 = Manager('Jonathan', 'Smilga',
                     50, 130000,
                     'jonathansmilga123@gmail.com'
                     )

employee_4 = Manager.employeeFromString("""
Aditya-Singh-15-200000-adityasingh27apr@gmail.com
""")

employee_5 = Manager.employeeFromString("""
Aditya-Singh-15-200000-adityasingh27apr@gmail.com
""")

# print("Before deleting ", employee_5)
# del employee_5  # to delete an instance

# print(len(employee_5))

# print(f"Is {employee_4} and Manager : {isinstance(employee_4, Manager)}")
# print(f"Is Every Employee an Manager {issubclass(Employee, Manager)}")

# employee_3.add_employee(employee_1)
# employee_3.add_employee(employee_2)

# employee_4.add_employee(employee_1)
# employee_4.add_employee(employee_2)
# employee_4.add_employee(employee_3)

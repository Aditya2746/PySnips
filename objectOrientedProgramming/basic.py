class Employee:
    incrementShouldGet = 1.05
    numberOfEmployee = 0

    def __init__(self, firstname, lastname, age, post, salary, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.post = post
        self.salary = salary
        self.email = email
        Employee.numberOfEmployee += 1

    def tellFullName(self):
        return f"{self.firstname} {self.lastname}"

    def raise_salary(self):
        self.salary = int(self.salary * self.incrementShouldGet)


employee_1 = Employee('John', 'Doe',
                      25, 'Junior Developer',
                      50000, 'johndoe123@gmail.com',
                      )
employee_2 = Employee('Ron', 'Michel',
                      35, 'Senior Developer',
                      110000, 'ronmichel123@gmail.com',
                      )
employee_3 = Employee('Jonathan', 'Smilga',
                      50, 'Senior Manager',
                      130000, 'jonathansmilga123@gmail.com',
                      )
employee_3.leads = [
                    employee_1.tellFullName(),
                    employee_2.tellFullName()
                ]

class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def tellFullName(self):
        return f"{self.firstname} {self.lastname}"

    @property
    def email(self):
        if self.firstname is not None and self.lastname is not None:
            return f"{self.firstname.lower()}{self.lastname.lower()}123@gmail.com"
        else:
            return "No Name provided"

    @tellFullName.setter
    def tellFullName(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @tellFullName.deleter
    def tellFullName(self):
        self.firstname = None
        self.lastname = None
        print("Name Deleted!!")


employee_1 = Employee('Aditya', 'Singh')

# print(employee_1.firstname)
# print(employee_1.lastname)

'''Changing name using setter'''
# print("Name Before changing ", employee_1.tellFullName)
# print("Email Before changing ", employee_1.email)
# employee_1.tellFullName = "John Doe"
# print("Name After changing ", employee_1.tellFullName)
# print("Email After changing ", employee_1.email)

'''Deleting name using deleter'''
# print("Name Before Deleting ", employee_1.tellFullName)
# print("Email Before Deleting ", employee_1.email)
# del employee_1.tellFullName
# print("Name After Deleting ", employee_1.tellFullName)
# print("Email After Deleting ", employee_1.email)

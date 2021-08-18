# just practising and following along with the class tutorials from
# Corey Schafer

import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1  # this raises the num of employees, to access later

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod  # this is an example of using class methods as alternative constructors.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # this is apparently a decorator
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):  # should be used for debugging or for usage of other developers
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # more readable; used to display for end user; fall backs on repr
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):  # this tells python how to add two employees together
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())




class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self. employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_enp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


employee_1 = Employee("Wormz", 'Short', 66000)
employee_2 = Employee('Charlie', 'Short', 78000)
dev_1 = Developer('Toto', 'Short', 100000, 'Javascript')
dev_2 = Developer('Bruce', 'Short', 90000, "Python")

mgr_1 = Manager('Lily', 'Short', 165000, [dev_2])

mgr_1.add_emp(dev_1)

isinstance(mgr_1, Manager)  # checks to see if this variable is part of a class

issubclass(Manager, Employee)  # checks to see if manager is a subclass of the first class

# emp_1 = Employee('Corey', 'Schafer', 5000)
# emp_2 = Employee('Bruce', 'Short', 6000)
#
# Employee.set_raise_amt(1.05)
#
# emp_str_1 = "John-Doe-7000"
# emp_str_2 = "Jamie-Jones-5500"
#
# first, last, pay = emp_str_1.split('-')
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.__dict__)
#
# my_date = datetime.date(2016, 7, 16)
#
# print(Employee.is_workday(my_date))

employees = [mgr_1,dev_2, dev_1]

def e_sort(emp):
    return emp.first

s_emp = sorted(employees, key=e_sort)

print(s_emp)

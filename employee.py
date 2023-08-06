"""Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase."""

# https://edabit.com/challenge/gB7nt6WzZy8TymCah

class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


    def fullname(self):
        fullname = self.name + self.lastname
        return fullname

    def email(self):
        email = f'{self.name}.{self.lastname}@gmail.com'
        return email
    
    def first_name(self):
        first_name = self.name
        return first_name
    
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")


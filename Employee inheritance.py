# Python code to demonstrate how parent constructors
# are called

# parent class
class Person( object ):
    #_init_is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
        def display(self):
            print(self.name)
            print(self.idnumber)

# child class
class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
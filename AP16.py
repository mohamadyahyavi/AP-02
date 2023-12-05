class Employee:
    def __init__(self,firstname,lastname,salary):
        
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
        
        
    @classmethod   
    def from_string(cls, emp_string):
        firstname, lastname, salary = emp_string.split('-')
        return cls(firstname, lastname, salary)

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.__dict__)
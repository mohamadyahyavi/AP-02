class Employee:
    def __init__(self,first_name:str,last_name:str):
        self.first_name=first_name
        self.last_name=last_name
        
    def email(self):
        
        return f"{self.first_name}.{self.last_name}@company.com"


    def fullname(self):
        
        return f"{self.first_name} {self.last_name}"
    
emp_1 = Employee("John", "Smith")
print(emp_1.fullname())
print(emp_1.email())    
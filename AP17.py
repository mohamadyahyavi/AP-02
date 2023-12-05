class Employee:
    def __init__(self, full_name, **kwargs):
        self.firstname, self.lastname = full_name.split()
        for key, value in kwargs.items():
            setattr(self, key, value)
            
            
            
            
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(john.firstname)
print(mary.lastname) 
print(richard.height)
print(giancarlo.nationality)            


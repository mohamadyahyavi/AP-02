class Person:
    def __init__(self,name:str,age:int):
        
        self.name=name
        self.age=age
        
    def compare_age(self,a):
        if self.age>a.age:
            return f"{a.name} is younger than {self.name}"
        elif self.age==a.age:
            
            return f"{a.name} is the same age as {self.name}"
        
        else:
             return f"{a.name} is younger than {self.name}"

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)

print(p1.compare_age(p2))
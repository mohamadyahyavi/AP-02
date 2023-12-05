import math 
class Circle:
    def __init__(self,radius):
        self.radius=radius
        
        
    def getArea(self):
        
       return  math.pow(self.radius,2)*math.pi
   
    
    def getPerimeter(self):
        
       return 2* self.radius * math.pi
   
    
   
     

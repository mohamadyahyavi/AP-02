class User:
    
    user_count=0
    
    def __init__(self,username):
        
        self.username=username
        User.user_count+=1
        
        
        
        
u1 = User("johnsmith10")
u2 = User("marysue1989")
print(User.user_count)        

# Q3. Explain why the __init__() function is used. Give a suitable example.

#__int()__ function is called as constructor function used to pass data to the object

class human:
    def __init__(self,name):
        self.name=name
        
obj=human("vaibhav")

print(obj.name)
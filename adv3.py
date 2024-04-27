# id means address
# pvm is responsible to provide value for self argument and we are not required to provide expilictly.
# for every object constructor gets executed only once
class Employee:
    college="gitam university" # static variables are class level variables
    def __init__(self,id,name): #__init__ is a constructor
        print("constructor execution")
        self.id=id # instance variable
        self.name=name # instance variable
    def hello(self): # Method and instance method
        name="nikith mint" # local variable.
        # self.name="tankashala"
        print("method execution")
        print(self.name)
        print(self.id)
    @classmethod    
    def getCollegeName(cls): # cls means class
        print("college Name",cls.college)
    @staticmethod    
    def findavg(x,y):   # static Methods
        print(x+y)
a=Employee(1,"nikith")
# b=Employee(2,"mint")
# c=Employee(3,"Tankashala")
a.hello()
print(Employee.college)
print(a.college)
Employee.getCollegeName()
Employee.findavg(10,20)
a.wife="renu" 
print(a.__dict__)
print(a.name,a.id)

# how to delete instance variables
# del.variablename inside the class
# del.objectreference.variablename

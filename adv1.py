# object oriented programming (oops)
# class (class is a blue print of the object)
# object (the physical existence of a class is nothing but object)
# reference variable
# once the class is ready we can create multiple objects.

class Student:
    def __init__(self,rollno,name): # init is a constructor
        self.rollno=rollno
        self.name=name
    def talk(self):
        print("hello my name is ",self.name)
        print("my Rollno is",self.rollno)

s=Student("100","nikith") # "s" is the reference variable where total sentence is the creation of the object
print(s.name)
print(s.rollno)
s.talk()

s1=Student(200,"mint")
s1.talk()





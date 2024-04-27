# 3 Types of variables
''' Static variables
    Instance Variables
    Local Variables'''
# 3 types of Methods
'''instance methods
    class methods
    static methods
                '''
class Test:
    f=10
    def __init__(self):
        print("inside constructor")
        print(Test.f)
        print(self.f)
        self.b=20
        self.c=30
    def m1(self):
        print("Inside Method")
        print(Test.f)
        print(self.f) 
        self.d=40
    @classmethod    
    def m2(cls):
        print("inside class")
        print(Test.f)
        print(cls.f)
t1=Test()
t1.m1() 
t2=Test()
t2.m2()

del t1.d           
print(t1.__dict__)

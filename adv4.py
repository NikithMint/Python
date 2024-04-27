# class Test:
#     def __init__(self):
#         print("welcome")
# a=Test()
# a=Test()
# a=Test()

# Overloaded Constructor (Concept is not available)
class Test:
    def __init__(self):
        print("no arg")
    def __init__(self,x):
        print("one-arg")    
t1=Test()
t2=Test(10)


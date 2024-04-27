class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hi",self.name)
        print("your marks are",self.marks)
    def grade(self):
        if self.marks>=60:
            print("first grade")
        elif self.marks>=50:
            print("second grade")
        elif self.marks>=35:
            print("third grade")
        else:
            print("failed")
a=Student("nikith",55)
a.grade()  
a.display()
                              
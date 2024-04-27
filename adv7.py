class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name    
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
s=student()
a=input()
b=int(input())
s.setName(a)
s.setMarks(b)
print(s.getName())
print(s.getMarks())

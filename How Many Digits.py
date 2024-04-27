li=[]
a=input()
li.extend(a)
count=0
for i in li:
    count=count+1
if count>3:
    print("More than 3 digits")
else:
    print(count)    
    
    
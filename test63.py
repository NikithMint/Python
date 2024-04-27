a=input()
list1=["a","e","i","o","u"]
list2=[]
list2.extend(a)
print(list2)
count=0
count1=0
count2=0
count3=0
count4=0
for i in list2:
    if i=="a" or i=="A":
        count=count+1
    if i=="e" or i=="E":
        count1=count1+1
    if i=="i" or i=="I":
        count2=count2+1
    if i=="o" or i=="O":
        count3=count3+1
    if i=="u" or i=="U": 
        count4=count4+1
if count>0:
    print("a is repeated",count)
if count1>0:
    print("e is repeated",count1)
if count2>0:
    print("i is repeated",count2)
if count3>0:
    print("o is repeated",count3)
if count4>0:
    print("u is repeated",count4)

               

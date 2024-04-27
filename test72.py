li=[]
a=input()
li.extend(a)
print(li)
count=0
count1=0
count2=0
count3=0
count4=0
for j in li:
    
    if j=="a":
        count=count+1
    elif j=="e":
        count1=count1+1
    elif j=="i":
        count2=count2+1
    elif j=="o":
        count3=count3+1
    elif j=="u":
        count4=count4+1
print(count)
print(count1)
print(count2)
print(count3)
print(count4)
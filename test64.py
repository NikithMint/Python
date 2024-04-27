a=int(input("Enter number of Elements to insert "))
li=[]
lii=[]
for i in range(a):
    b=int(input())
    li.append(b)
li.sort()
print(li)    
for k in li:
    if k%2==0:
        lii.append(k)
print(lii)

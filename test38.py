import math


a=int(input())
li=[]
lii=[]
for i in range(a):
    b=int(input())
    li.append(b)
    if len(li)==a:
        break
for f in li:
    for k in range(2,10000):
        if f==(k*k):
            lii.append(f)
        
v=0         
for m in lii:
    v=math.sqrt(m)+v
print(v)            
            

            

        

    
        
   

a=int(input())
li=[]
lii=[] 
liii=[] 
for i in range(a*2):
    x = list(map(int,input().split(" ")))
    li.append(x)
    
    if len(li)==a*2:
        break
for k in li:
    count=0
    if k[0]==1 and k[1]==1 and k[2]==1:
        count=3
        lii.append(count)
    elif k[0]==1 and k[1]==0 and k[2]==1:
        count=2
        lii.append(count) 
    elif k[0]==1 and k[1]==0 and k[2]==0:
        count=1
        lii.append(count)
    elif k[0]==0 and k[1]==0 and k[2]==1:
        count=1
        lii.append(count)
    elif k[0]==0 and k[1]==1 and k[2]==0:
        count=1
        lii.append(count)
    elif k[0]==0 and k[1]==1 and k[2]==1:
        count=2
        lii.append(count)
    elif k[0]==1 and k[1]==1 and k[2]==0:
        count=2
        lii.append(count)    
    else:
        count=0
        lii.append(count) 

for k in li:
    count1=0
    
    for j in range(3):
        
        
        
        if k[j]==0 :
            count1=count1+1
    liii.append(count1)

print(lii)
print(liii)    
              
if lii[0]==lii[1] and liii[0]==liii[1] :
    print("Pass")
else:
    print("fail")    
if lii[2]==lii[3] and liii[2]==liii[3] :
    print("Pass")    
else:
    print("Fail")
    
           

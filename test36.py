a=int(input())
li=[]
lii=[] 
one=[]
zero=[]
for i in range(a):
    x = list(map(int,input().split(" ")))
    li.append(x)
    y= list(map(int,input().split(" ")))
    lii.append(y)
for k in li:
    count3=0
    q=len(li[0])
    for j in range(q):
        
        
        
        if k[j]==1 :
            count3=count3+1
    one.append(count3)    

for k in lii:
    count4=0
    w=len(lii[0])
    
    for j in range(w):
        
        
        
        if k[j]==1 :
            count4=count4+1
    one.append(count4)    
    

#-----------------
for k in li:
    count2=0
    e=len(li[0])
    for j in range(e):
        
        
        
        if k[j]==0 :
            count2=count2+1
    zero.append(count2)

#--------------
for k in lii:
    count1=0
    r=len(lii[0])
    for j in range(r):
        
        
        
        if k[j]==0 :
            count1=count1+1
    zero.append(count1)

print(li)
print(lii)
print(one)
print(zero)
if a==1:
    if one[0]==one[1] and zero[0]==zero[1]:
        print("Pass")
    else:
        print("Fail")



if a>1:
    if one[0]==one[2] and zero[0]==zero[2] :
        print("Pass")
    else:
        print("Fail")
    if one[1]==one[3] and zero[1]==zero[3] :
        print("Pass")    
    else:
        print("Fail")
   

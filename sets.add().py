a=int(input())
l1=[]
l2=[]
for i in range(a):
    b=list(map(str,input()))
    l1.append(b)
for k in l1:
    if k not in l2:
        l2.append(k)
count=0        
for k in l2:
    count=count+1
print(count)            

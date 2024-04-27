n=int(input())
li=[]
lii=[]
for i in range(n):
    x=int(input())
    li.append(x)
    if len(li)==n:
        break
for j in li:
    if j>=300:
        a=j*10
        lii.append(a)
        
    else:
        k=3000
        lii.append(k)  


for k in lii:
    print(k)


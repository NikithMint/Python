lii=[]
a=list(map(int,input().split(" ")))
lii.append(a)
li=[]
liii=[]
for i in range(lii[0][1]):
    b=list(map(float,input().split(" ")))
    li.append(b)
for k in range(lii[0][0]):
    sum=0
    for j in range(lii[0][1]):
        c=li[j][k]
        sum=sum+c
    liii.append(sum)
print(liii)           
for l in liii:
    d=l/lii[0][1]
    print(d)
    




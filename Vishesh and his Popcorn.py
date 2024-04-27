a=int(input())
li=[]
lii=[]
for i in range(a*3):
    b=list(map(int,input().split(" ")))
    li.append(b)
print(li)    
for j in range(len(li)):
    c=li[j][0]+li[j][1]
    lii.append(c)
chunk_size=3
d=[lii[k:k + chunk_size] for k in range(0,len(lii),chunk_size)]
for l in range(len(d)):
    print(max(d[l]))

    




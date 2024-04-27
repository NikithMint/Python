# li=[1,2,3,4,5,6,7]
# sum=0
# for i in li:
#     sum=sum+i
# print(sum)

a=int(input())
li=[]
lii=[]
liii=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)): # 0 1 2
    c=li[j][0]+li[j][1]
    lii.append(c)
for k in range(len(lii)):
    count=0
    if lii[k]==lii[k]:
        count=count+1
        liii.append(count)
    elif lii[k]!=lii[k]:
        liii.append(0)    
for m in liii:
    if m==1:
        print("YES")
    else:
        print("NO")    







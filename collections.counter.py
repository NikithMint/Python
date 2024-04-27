from collections import Counter
a=int(input())
b=list(map(int,input().split(" ")))
c=int(input())
l1=[]
l2=[]
for i in range(c):
    d=list(map(int,input().split(" ")))
    l1.append(d)
for k in l1:
    if k not in l2:
        l2.append(k)
sum=0
for j in range(len(l2)):
    e=l2[j][1]
    f=l2[j][0]

    if f in b :
        sum=sum+e
print(sum)




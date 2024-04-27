a=int(input())
l1=[]
l2=[]
for i in range(a):
    b=int(input())
    l2.append(b)
    c=list(map(int,input().split(" ")))
    l1.append(c)
for j in range(len(l1)):
    for k in range(len(l1[j])):
        d=l1[j][k]
        e=l1[j][l2[j]-1-k]

        print(e)



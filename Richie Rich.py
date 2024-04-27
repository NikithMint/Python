a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    c=li[j][1]-li[j][0]
    d=c//li[j][2]
    print(d)


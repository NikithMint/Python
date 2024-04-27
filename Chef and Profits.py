a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    c=li[j][0]*li[j][1]
    d=li[j][0]*li[j][2]
    e=c-d
    print(e)

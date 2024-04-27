a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    c=li[j][0]*li[j][3]/100
    d=li[j][0]+(c)
    if li[j][1]<=d<=li[j][2]:
        print("YES")
    else:
        print("NO")        
a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    c=li[j].sort() 
    d=li[j][1]+li[j][2]
    print(d) 
    
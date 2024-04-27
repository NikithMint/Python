#---------Farmer And His Plot--------------#
a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
print(li)    
for j in range(len(li)):
    a=li[j][1]
    b=li[j][0]-1
    c=a-b
    d=c*li[j][2]
    print(d)
    



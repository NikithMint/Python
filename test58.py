a=int(input())
li=[]
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    for j in range(len(d)):
        if d[j]==0:
            li.append(c[j])
# for k in range(len(li)):
#     e=min(li[k])
#     print(e)
print(li)
            
    


from unittest import result


a=int(input())
li=[]
  
 

for i in range(a):
    x = list(map(float,input().split(" ")))
    li.append(x)
    
    if len(li)==a*2:
        break


for k in li:
    b=k[0]*k[0]
    c=k[2]*k[2]*k[2]
    d=k[1]*k[1]
    e=k[3]*k[3]*k[3]
    res=b/c
    res1=d/e
    if res==res1:
        print("YES")
    else:
        print("NO")    

li=[]
q,n=list(map(int,input().split(" ")))
for i in range(n,q+1):
    li.append(i)
sum=0
prod=1
for j in li:
    sum=sum+j
    prod=prod*j
print(sum)    
print(prod)

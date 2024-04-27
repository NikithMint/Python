
n=int(input())
li=[]
for i in range(n):
    a=list(map(int,input().split(" ")))
    li.append(a)
   
for j in li:
    b=j[0]+j[0]*j[2]
    c=j[1]+j[3]*j[0]
    
    if b>c:
        print("Chefina")
    if c>b:
        print("Chef")
    if b==c:
        print("Draw")    


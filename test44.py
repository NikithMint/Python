n=int(input())
li=[]
for i in range(n):
    a=list(map(int,input().split(" ")))
    li.append(a)
    if len(li)==n:
        break
for j in li:
    b=(j[0]+180)*2
    c=j[1]+j[2]
    d=b-c
    
    print(d) 
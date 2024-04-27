n=int(input())
li=[]
lii=[]
liii=[]

for i in range(n):
    for j in range(3):
        a=list(map(int,input().split(" ")))
        li.append(a)

for k in range(1):
    for o in li:
        b=o[0]+o[1]
        lii.append(b)
for w in range(n):
    for m in lii:
        liii.append(m)
        if len(liii)==n*3:
            break

print(liii)    
liii.sort()
print(liii[2])
          
        




    



        

   


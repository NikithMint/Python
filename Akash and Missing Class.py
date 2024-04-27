a=int(input())
li=[]
for i in range(a):
    b=int(input())
    if b<0:
        d=0
        li.append(d)
    else:
        c=(b+1)//7
        li.append(c)
for j in li:
    print(j)    
      
# M T W TH F SAT SU
# 1 2 3 4  5 6   7

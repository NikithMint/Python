# AIRLINE RESTRICTIONS.................
a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
    
for j in range(a):
    
    a=li[j][0]+li[j][2]
    if a<=li[j][3] and li[j][1]<=li[j][4]:
        print("YES")
    else:
        print("NO")    

    
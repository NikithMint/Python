####---------------------Reach fast----------------------------####
import math
a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in li:
    if j[0]>j[1]:
        c=j[0]-j[1]
        d=abs(math.ceil(c/j[2]))
        print(d)
    elif j[1]>j[0]:
        e=j[1]-j[0]
        f=abs(math.ceil(e/j[2]))
        print(f)
    else:
        print("0")    




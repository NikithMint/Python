import math
from math import comb
a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    a=(li[j][0]-1)
    b=(li[j][1]-1)
    print(a)
    print(b)
    c=math.factorial(a)
    d=math.factorial(b)
    e=(c-d)
    f=e*d
    g=c/f
    print(g)       

    
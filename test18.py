# from ast import Pass


# for i in range(3):
#     for j in range(1):
#         print(j)
#         print(i)
        




# #--------------------------------
# print("gitam",end='')
# print("University")




# #---------------------------------
# #prime number # 3 5 7 13
# x=int(input("Enter a number"))
# if x>1:
#     for i in range(x):
       
#         if i%x==0:
#             print("it is a prime number")
#             break
#         else:
#             print("it is not a prime number")    
# else:
#     print("it is a prime number")

    
#----------------------------------

# from audioop import reverse

# Largest Number-----------------------------------
# y=[]
# start=int(input("enter a number"))

# for i in range(start):
#     z=int(input("enter numbers"))
#     y.append(z)
    
# y.sort(reverse=True)
# print(y[0])



#------------------------------------------------

from ast import Pass
from cmath import nan
from ctypes import sizeof


def print_well():
    print("hello")
print_well()    

#-------------------

# summ=[]
# no=int(input("total no of numbers to insert"))
# sum=0
# for i in range(no):
#     # g=int(input("enter numbers"))
#     # summ.append(g)
#     sum=sum+i
# print(sum) 



lam= lambda a: a+50
print(lam(100))

str="nikith"
print(str[:1])
print(str[::1])

#---------------pascals Triangle
a=[]
b=[]
c=[]
d=[]
e=[]

for i in range(1):
    f=int(input("enter a numbers in 1st list"))
    a.append(f)
    break
for j in range(2):
    g=int(input("enter a numbers in 2nd list"))
    b.append(g)
    if len(b)==2:
        break
    
for k in range(3):
    l=int(input("enter a numbers in 3rd list"))
    c.append(l)
    if len(c)==3:
        break
c[1]=b[0]+b[1]


for m in range(4):
    n=int(input("enter a number in 4th list"))
    d.append(n)
    if len(d)==4:
        break
d[1]=c[0]+c[1]
d[2]=c[1]+c[0]

for t in range(5):
    o=int(input("enter a number in 5th list"))
    e.append(o)
    if len(e)==5:
        break
e[1]=d[0]+d[1]
e[2]=d[1]+d[2]
e[3]=d[2]+d[3]    
print(a)
print(b)
print(c)
print(d)
print(e)

#---------------------------------------












    



    










     









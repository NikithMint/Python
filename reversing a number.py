x=int(input())
# lii=[]
# while (x>0):
#     dig=x%10
#     lii.append(dig)
#     x=x//10
# com=int(''.join(map(str,lii)))
# print(com)

a=str(x)
li=[]
li.extend(a)
b=li[::-1]
b.pop(len(li)-1)
b.insert(0,li[0])
print(b)
if b[0]=="-":
    for i in b:
        print(i,end="")
else:
    for j in li:
        print(j,end="")
        

               
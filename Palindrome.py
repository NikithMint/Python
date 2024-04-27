# from typing import OrderedDict


# n=int(input())
# li={}
# for i in range(n):
#     a=int(input("Enter account no"))
#     b=input("Enter name")
    
#     li[a]=b
# print(li)
# c=sorted(li.items(), key=lambda li: li[0])
# print(c)
# print()

n=input()
li=[]
lii=[]
liii=[]
li.append(n)
for i in li:
    lii.extend(i)
for j in range(len(lii)):
    liii.append(lii[::-1])
    if len(liii)==1:
        break
for k in range(len(lii)):
    if lii[k]==liii[0][k]:
        print("it is a palindrome")
        exit()
    else:
        print("Not a palindrome")
        break





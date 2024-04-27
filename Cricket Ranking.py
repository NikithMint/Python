
# Difficulty Rating 996
a=int(input())
li=[]
lii=[]
for i in range(a*2):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in li:
    c=j[0]+j[1]+j[2]
    lii.append(c)

print(lii)
for l in range(0,len(lii),2):
    if lii[l]>lii[l+1]:
        print("A")
    else:
        print("B")  

#-------------important-------------#
# for i in range(0,6,2):
#     print(i,i+1)
# 0 1
# 2 3
# 4 5
# [0 1 2 3 4 5]    
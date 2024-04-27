# cook your dish here
n = int(input())
li = []
lii = []
for i in range(n):
    a = list(int(i) for i in input().split(" "))
    li.append(a)
    if len(li) == n:
        break
for j in li:
    if j[0] > j[1]:
        a = j[0]-j[1]
        lii.append(a)
    else:
        b = j[1]-j[0]
        lii.append(b)
        
for k in lii:
    print(k)

# lam= lambda a: a+50
# print(lam(100))
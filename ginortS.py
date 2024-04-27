l1=[]
l2=[]
a=input()
l1.extend(a)
print(l1)
l1.sort()
print(l1)
for i in l1:
    if i.islower():
        l2.append(i)
for k in l1:
    if k.isupper():
        l2.append(k)
for j in l1:
    if j.isnumeric() and int(j)%2!=0:

        l2.append(j)
for n in l1:
    if n.isnumeric() and int(n)%2==0:
        l2.append(n)
for m in l2:
    print(m,end="")

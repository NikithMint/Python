from collections import Counter
a=input()
b=input()
l1=[]
l2=[]
l1.extend(a)
l2.extend(b)
l1.sort()
l2.sort()
c=Counter(a)
d=Counter(b)
count=0
for i in c:
    for j in d:
        if i==j:
            count=count+1
if len(c)==count:
    print("true")
else:
    print("false")
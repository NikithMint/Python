a=int(input())
l1=[]
for i in range(a):
    b=list(map(str,input()))
    l1.append(b)
for j in range(len(l1)):
    count=0
    count1=0
    count2=0
    count3=0
    l2=[]
    for k in l1[j]:
        count2=count2+1
        if k.isupper() and k.isalnum():
            count=count+1
        elif k.isdigit() and k.isalnum():
            count1=count1+1
    for m in l1[j]:
        if m not in l2:
            l2.append(m)
    for n in l2:
        count3=count3+1
    if count3==10 and count2==10 and count1>=3 and count>=2:
        print("Valid")
    else:
        print("Invalid")







    
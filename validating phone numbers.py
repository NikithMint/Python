a=int(input())
l1=[]
for i in range(a):
    b=list(map(str,input()))
    l1.append(b)
for j in range(len(l1)):
    count1=0
    count2=0
    count3=0
    for k in l1[j]:
        count1=count1+1
        if k.isdigit():
            count2=count2+1
    for m in range(1):
        if l1[j][0]=="7" or l1[j][0]=="8" or l1[j][0]=="9":
            count3=count3+1
    if count1==10 and count2==10 and count3==1:
        print("YES")
    else:
        print("NO")    

            
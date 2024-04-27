a=int(input())
li=[]
for i in range(a):
    b=list(map(str,input()))
    li.append(b)
for k in range(a):
    count=0
    count1=0
    for j in range(len(li[k])):
        if li[k][j]=="a":
            count=count+1
        else:
            count1=count1+1
    if count>count1:
        print(count1)
    else:
        print(count)

          

        

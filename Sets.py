a=int(input())
li=[]
b=list(map(int,input().split(" ")))
li.append(b)
print(li)
for i in li[0]:
    if li[0].count(i)==1:
        print(i)



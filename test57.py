a=int(input())
li=[]
for i in range(a):
    b=int(input())
    li.append(b)
print(li)    
for j in range(a):
    if li[j]>=2000:
        print("Yes")
    elif li[j]<2000:
        print("No")


    

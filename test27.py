from operator import contains


a=int(input())
li=[]
for i in range(0,a):
    b=input()
    li.append(b)
    if len(li)==a:
        break
print(li)  
fli=[]
count=0
for i in li:
    if i not in fli:
        a = fli.append(i)
        count=count+1
        if len(fli)==a:
            break
print(count)

count1=1
for k in li:
    if k in li:
        count1=count1+1
        
print(count1,end="")
print(li)

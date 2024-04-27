a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    if li[j][1]<=li[j][0]<=li[j][2]:
        print("Take second dose now")
    elif li[j][0]>li[j][2]:
        print("Too Late")
    elif li[j][0]<li[j][2]:
        print("Too Early")
        
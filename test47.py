a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
    if len(li)==a:
        break
for j in li:
    c=j[0]+j[2]
    d=j[1]+j[3]
    if c>d:
        print("N")
    elif c==d:
        print("N")
    else:
        print("S")



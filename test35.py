a=int(input())
li=[]
  
 

for i in range(a):
    x = list(map(float,input().split(" ")))
    li.append(x)
    
    if len(li)==a*2:
        break

for k in li:
    a=k[2]/k[0]
    b=k[3]/k[1]
    if a<b:
        print("-1")
    elif a==b:
        print("0")
    else:
        print("1")        
      
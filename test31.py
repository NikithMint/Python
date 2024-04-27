a=int(input())
li=[]

for i in range(a):
    x = list(map(str,input().split(" ")))
    li.extend(x)
    
    if len(li)==a:
        break

for x in li:
    k = [int(a) for a in str(x)]
    count=0
    for i in k:
        
        
        
        if i==4:
            count=count+1
    print(count)
            
    
              




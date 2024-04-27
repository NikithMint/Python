from ctypes import sizeof


a=int(input())
li=[]
  
 

for i in range(a):
    x = list(map(int,input().split(" ")))
    li.append(x)
    
    if len(li)==a*2:
        break

  

for k in li:
    flag=0
     
    if k[0]==k[1]:
        print("YES")
          
    elif k[0]>k[1]:
        k[0],k[1]=k[0],k[1]
    else:        
        k[0],k[1]=k[1],k[0]
    while k[0]>k[1]:
        k[1]=k[1]*2
        if k[0]==k[1]:
            flag=1
    if flag==0 :
        print("NO")
    else:
        print("YES")            
        
            
# a="hello"
# print(a[::-1])

a=int(input())
li=[]
lii=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    c=li[j][0]+li[j][1]
    lii.append(c)
  
for k in lii:
    sum=0
    while(k>0):
        
        dig=k%10
        if dig==0 or dig==6 or dig==9: #6666
            sum=sum+6
        elif dig==2 or dig==3 or dig==5:
            sum=sum+5
        elif dig==1:
            sum=sum+2 
        elif dig==4:
            sum=sum+4
        elif dig==7:
            sum=sum+3
        elif dig==8:
            sum=sum+7                   
        k=k//10
    print(sum)    
    
    


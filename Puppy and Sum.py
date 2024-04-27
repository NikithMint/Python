a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split()))
    li.append(b)
print(li)  
for j in range(len(li)):
    for m in range(li[j][0]):
        sum=0
        for k in range(li[j][1]+1):
            sum=sum+k
        li[j][1]=sum
    print(sum)

        
    

         

    


        
    
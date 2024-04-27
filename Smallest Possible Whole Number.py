# a=int(input())
# li=[]
# lii=[]
# for i in range(a):
#     b=list(map(int,input().split(" ")))
#     li.append(b)
   
# for k in range(len(li)):
#     if li[k][0]>li[k][1]:
#         d=li[k][0]//li[k][1]
        
#         c=li[k][0]-li[k][1]
#         lii.append(c)
#         for m in range(d-1):
            
#             e=lii[m]-li[k][1]
            
#             lii.append(e)
#         print(lii[::-1][0])           
#     if li[k][0]==li[k][1]:
#         print("0")
#     if li[k][0]<li[k][1]:
#         print(li[k][0])

a=int(input())
li=[]
for i in range(a):
    b=list(map(int,input().split(" ")))
    li.append(b)
for j in range(len(li)):
    if li[j][1]!=0:
        c=li[j][0]%li[j][1]
    print(c)
    
    

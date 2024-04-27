
# for i in range(1,6):
#     for j in range(i):
        
#         print(i,end="")
       
    

   

#-------------------
from posixpath import split
#---------------------------------
#---------------------------------phone number problem------------------------------------------     
# li=[]
# x=int(input())
# for i in range(x):
#     y=input()
#     li.extend(y)

  
# for j in range(0,len(li),10):
#     if int(li[j])==9 or int(li[j]) ==7 or int(li[j])==8 and len(li[j])==10*x:
#         print("YES")   
           
#     else:
#         print("NO")        
        

#------------------------------------------------------------------------------------------------
li=[]
x=int(input("enter number of numbers to enter"))
for i in range(x):
    y=input("enter numbers")
    li.append(y)
    if len(li)==3:
        break
print(li)



for j in range(len(li)):
    if (float(li[j])==True):
        print("True")
    else:
        print("False")    


#------------------- or --------------------------------#
# for i in range(int(input())):    
#     try:
#         n=input()
#         int(n.split('.')[1])	
#         if float(n):
#             print('True')
#     except:        
#         print('False')




#-----------------------------------------------------------------
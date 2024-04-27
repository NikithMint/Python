# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
  
# # Initialize matrix
# matrix = []
# print("Enter the entries rowwise:")
  
# # For user input
# for i in range(R):          # A for loop for row entries
#     a =[]
#     for j in range(C):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)
  
# # For printing the matrix
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end = " ")
#     print()
#     break


from array import array
from multiprocessing.connection import wait


arrr=[]
x=int(input("enter length of an array"))

for i in range(x):
    y=int(input("enter array elements"))
    arrr.append(y)
    if len(arrr)==x:
        break

print(arrr)    
count=0
for j in arrr:
    if j>0:
        count=count+1
print(count/len(arrr))






  


    

    

    


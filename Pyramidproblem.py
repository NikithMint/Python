# pyramid problem
#    * 
#   * *
#  * * *
# * * * *

n=4
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

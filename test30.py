# a = ["1", "2", "-3"]
# ints = []
# for element in a:
#     ints.append(int(element))
# print(ints)
#-----------CHEAPER CAB----------#
# n=int(input())
# li = []
# for i in range(0,n):
#     x = list(map(int, input("Enter multiple values: ").split()))
#     li.append(x)
#     if len(li)==n:
#         break
# for k in li:
#     if k[0]>k[1]:
#         print("SECOND")
#     elif k[0]<k[1]:
#         print("FIRST")
#     else:
#         print("ANY")         

#-------------MAXIMUM SUBMISSIONS------------------#
n=int(input())
li=[]
for i in range(n):
    a=int(input())
    li.append(a)
for j in li:
    b=j*2
    print(b)
    











    


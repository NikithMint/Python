# HOT OR COLD

# x=int(input())
# li=[]
# for i in range(x):
#     a=int(input())
#     li.extend(a)
#     if len(li)==x:
#         break
# for j in li:
#     if j>20:
#         print("HOT")
#     else:
#         print("COLD")
li=[]
y=int(input())
for i in range(y):
    x = list(map(int, input().split()))
    li.append(x)
    if len(li)==y:
        break
print(li[0][1]-li[0][0])
print(li[1][0]-li[1][1])






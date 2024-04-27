nums=[0,1,2,2,3,0,4,2]
l1=[]
val=2
b=len(nums)
for i in range(b):
    if val!=nums[i]:
        l1.append(nums[i])
print(l1)
   
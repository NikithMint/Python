nums=[1,2,3,1]
nums.sort()
print(nums)
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[i]==nums[i-1]:
            print("True")
        else:    
            print("False")
            
            
                
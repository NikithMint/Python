import math
nums1=[1,2]
nums2=[3,4,5,6,7,8,9,10,11]
nums3=nums1+nums2
nums3.sort()
a=math.floor(len(nums3)/2)
if len(nums3)%2==0:
    e=float(len(nums3)/2-1)
    f=float(e+1)
    
    b=nums3[e]
    c=nums3[f]
    print(b)
    print(c)
    d=b+c
    g=d/2
    print(g)
else:
    print(nums3[a])


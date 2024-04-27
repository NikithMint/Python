li=[]
x=int(input("enter no of mobile numbers"))
for i in range(x):
    y=input("enter a mobile number")
    li.extend(y)
print(li)
  
for j in range(x):

    
    if li[0]==9 or li[0]==7 or li[0]==8:
        print("YES")
    elif li[10]==9 or li[10]==7 or li[0]==8 :
        print("YES")  
    else:
        print("NO")        


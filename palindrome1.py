a=int(input("Enter a Number"))
temp=a
rev=0
while(a>0):
    dig=a%10
    
    rev=rev*10+dig # rev=rev+dig**3 for Amstrong number
    a=a//10
print(rev)
if temp==rev:
    print("it is a palindrome")
else:
    print("its is not a palindrome")        

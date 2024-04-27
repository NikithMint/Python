a=int(input())
count=0
for i in range(1,a):
    print(i)
    if a%i==0:
        count=count+1
if count==1:
    print("prime number")
elif a==1:
    print("not a prime number")     
else:
    print("not a prime number")         

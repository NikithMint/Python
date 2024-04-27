# for i in range(1,101):
#     count=0
#     for j in range(2,(i//2+1)):
#         if i%j==0:
#             count=count+1
#             break
#     if count==0 and i!=1:
#         print(i)    


num = 15
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    print((num//2))
    for i in range(2, int(num/2)+1):
        
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        print(i)
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
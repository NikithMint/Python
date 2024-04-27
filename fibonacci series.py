n=int(input())
a=0
b=1
if n<=0:
    print(a)
else:
    for x in range(n):
        c=a+b
        print(c)
        a=b
        b=c
        
            
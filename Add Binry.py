a=list(map(int,input()))
b=list(map(int,input()))
l1=a[::-1]
l2=b[::-1]
sum1=0
for i in range(len(l1)):
    c=2**i*l1[i]
    sum1=sum1+c
sum2=0
for j in range(len(l2)):
    d=2**j*l2[j]
    sum2=sum2+d
e=sum1+sum2
print(format(e,"08b"))

    


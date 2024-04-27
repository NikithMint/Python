import math
li=[0,0.5,0.07,0.8,1]
a=int(input())
b=int(input())
c=a*a+b*b
AC=math.sqrt(c)
theta=math.acos(b/AC)
print(math.degrees(theta))
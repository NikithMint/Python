s="nikith tankashala mint"
li=[]
sub=s.split()
print(sub)
print(s.upper())
print(s.swapcase())
for i in range(1):
    li.extend(s)
for j in range(len(s),0,-1):
    print(li[j-1],end="")
       

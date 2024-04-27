s="abbababababacdefg"
sub="ab"
li=[]
for i in range(1):
    li.extend(s)
print(li)
for j in range(len(li)):
    if li[j]==sub:
        print("Found at position",j)
print(s.count("ab"))   

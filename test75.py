li=['n','i','k','i','t','h']
count={}
for j in li:
    if j not in count:
        count[j]=1
    else:
        count[j]+=1 
print(count)          

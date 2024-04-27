# REMOVING DUPLICATE ELEMENTS IN A LIST

fli=[]
li=[1,1,3,5,4,3,7]
for i in li:
    if i not in fli:
        a = fli.append(i)
print(fli)        


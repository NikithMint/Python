a=input()
li=[]
if 100000<=int(a)<=999999:
    li.extend(a)
if li[0]==li[2] or li[2]==li[4]:
    print("False")
elif li[1]==li[3] or li[3]==li[5]:
    print("False")        
else:
    print("True")


